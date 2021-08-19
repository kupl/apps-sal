# class Solution:
#   def lenLongestFibSubseq(self, A: List[int]) -> int:
#     aSet = set(A)
#     ans = 0
#     for i in range(len(A)):
#       for j in range(i+1, len(A)):
#         x, y = A[j], A[i] + A[j]
#         length = 2
#         while y in aSet:
#           x, y = y, x + y
#           length += 1
#         ans = max(ans, length)
#     return ans if ans >= 3 else 0

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        aSet = set(A)
        dp = collections.defaultdict(int)
        ans = 0
        for i in range(len(A)):
            for j in range(i):
                if A[i] - A[j] < A[j] and A[i] - A[j] in aSet:
                    dp[(A[j], A[i])] = dp.get((A[i] - A[j], A[j]), 2) + 1

        return max(dp.values() or [0])
