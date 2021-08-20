class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        my_set = [set([A[i]]) for i in range(len(A))]
        ans = set(A)
        for i in range(1, len(A)):
            for prev_result in my_set[i - 1]:
                res = A[i] | prev_result
                my_set[i].add(res)
                ans.add(res)
        return len(ans)
