class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        ctr = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if ctr[A[j]] == 0:
                K -= 1
            ctr[A[j]] += 1
            while K < 0:
                ctr[A[i]] -= 1
                if ctr[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res
        
#         count = collections.Counter()
#         res = i = 0
#         for j in range(len(A)):
#             if count[A[j]] == 0: K -= 1
#             count[A[j]] += 1
#             while K < 0:
#                 count[A[i]] -= 1
#                 if count[A[i]] == 0: K += 1
#                 i += 1
#             res += j - i + 1
#         return res

