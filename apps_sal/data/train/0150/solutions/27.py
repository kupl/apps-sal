class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        ans = 1
        all_max = A[0]
        curr_max = 0
        for i in range(len(A)):
            curr_max = max(curr_max, A[i])
            if all_max > A[i]:
                all_max = curr_max
                ans = i + 1
        return ans
