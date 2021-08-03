class Solution:
    def numTriplets(self, A: List[int], B: List[int]) -> int:
        res = 0

        def count(n2, arr):
            res = 0
            c = defaultdict(int)
            for n in arr:
                if n2 % n == 0:
                    res += c[n2 // n]
                c[n] += 1
            return res

        for i, n in enumerate(A):
            res += count(n * n, B)
        for i, n in enumerate(B):
            res += count(n * n, A)
        return res


#         A.sort()
#         B.sort()
#         n, m = len(A), len(B)
#         res = 0

#         def perm(same):
#             if same <= 2:
#                 return 1
#             return (same - 1) * same // 2

#         def loop_me(arr, t, m, target):
#             res = 0
#             l, r = 0, m - 1
#             while l < r:
#                 tmp = arr[l] * arr[r]
#                 if tmp > t:
#                     r -= 1
#                 elif tmp < t:
#                     l += 1
#                 else:
#                     same = 0
#                     for k in range(l, r + 1):
#                         if arr[k] == arr[r]:
#                             same += 1
#                             # print(k, r)
#                         else:
#                             break
#                     print(\"--\", target, same, perm(same))
#                     # print(same)
#                     res += perm(same)
#                     break
#             return res

#         for i in range(n):
#             t = A[i] * A[i]
#             res += loop_me(B, t, m, A[i])

#         for i in range(m):
#             t = B[i] * B[i]
#             res += loop_me(A, t, n, A[i])

#         return res
