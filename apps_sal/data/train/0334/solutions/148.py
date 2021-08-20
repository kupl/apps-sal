class Solution:

    def minCost(self, S: str, B: List[int]) -> int:

        def if_continues_char(ind):
            return S[ind] == S[ind + 1]

        def consecutive_char(ind):
            consecutive_cost = B[ind]
            min_cost = B[ind]
            while ind < len(S) - 1 and S[ind] == S[ind + 1]:
                ind += 1
                consecutive_cost += B[ind]
                min_cost = max(min_cost, B[ind])
            return (ind + 1, consecutive_cost - min_cost)
        if not S or not B:
            return 0
        (i, cost) = (0, 0)
        while i < len(S) - 1:
            if if_continues_char(i):
                (i, del_cost) = consecutive_char(i)
                cost += del_cost
            else:
                i += 1
        return cost
