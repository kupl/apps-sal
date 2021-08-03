# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         def segment_sum(x,k):
#             # x is worst case, k is number of eggs available
#             # returns max N for worst case x, eggs k
#             if k==1:
#                 return x
#             return sum(segment_sum(j, k-1)+1 for j in range(x))

#         worst_case=0
#         while segment_sum(worst_case, K) < N:
#             worst_case+=1
#         return worst_case

# class Solution(object):
#     def superEggDrop(self, K, N):
#         drops = 0                           # the number of eggs dropped
#         floors = [0 for _ in range(K + 1)]  # floors[i] is the number of floors that can be checked with i eggs

#         while floors[K] < N:                # until we can reach N floors with K eggs

#             for eggs in range(K, 0, -1):
#                 floors[eggs] += 1 + floors[eggs - 1]
#             drops += 1

#         return drops

# class Solution(object):
#     def superEggDrop(self, K, N):
#         def f(x):
#             ans = 0
#             r = 1
#             for i in range(1, K+1):
#                 r *= x-i+1
#                 r //= i
#                 ans += r
#                 if ans >= N: break
#             return ans

#         lo, hi = 1, N
#         while lo < hi:
#             mi = (lo + hi) // 2
#             if f(mi) < N:
#                 lo = mi + 1
#             else:
#                 hi = mi
#         return lo

from scipy.special import comb, factorial, hyp2f1
from math import log2, floor


def h(k, n):
    return round(2**n - 1 - comb(n, k + 1) * hyp2f1(1, k - n + 1, k + 2, -1))


def h2(k, n):
    return sum(comb(n, j) for j in range(1, k + 1))


def e(k, n):
    if k == 1:
        return n
    return sum(e(k - 1, j) + 1 for j in range(n))


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        best_case = floor(log2(n) + 1)
        if k >= best_case:
            return best_case
        l = 0
        while h2(k, l) < n:
            l += 1
        return l
