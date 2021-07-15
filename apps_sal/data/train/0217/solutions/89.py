class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur,res = set(),set()
        for i in A:
            cur = { i|j for j in cur} | {i}
            res |= cur
        return len(res)
#        nums, n = set(), len(A)
#        for i in range(n):
#            num = A[i]
#            for j in range(i, n):
#                num |= A[j]
#                nums.add(num)
#        return len(nums)

