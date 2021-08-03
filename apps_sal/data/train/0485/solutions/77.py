

class Solution:
    def minKBitFlips(self, A, K):
        cur, res, n = 0, 0, len(A)
        for i in range(len(A)):
            if i >= K and A[i - K] > 1:
                A[i - K] -= 2
                cur -= 1
            if cur & 1 ^ A[i] == 0:
                if i + K > len(A):
                    return -1
                A[i] += 2
                cur += 1
                res += 1
        return res


# class Solution:
#     def minKBitFlips(self, A: List[int], K: int) -> int:
#         cnt = 0
#         for i in range(len(A) + 1 - K):
#             if A[i] == 0:
#                 cnt += 1
#                 for k in range(K):
#                     A[i+k] ^= 1
#             else:
#                 continue
#         return cnt if 0 not in A[-K:] else -1
