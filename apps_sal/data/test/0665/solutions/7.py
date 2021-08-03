"""#!/usr/bin/env pypy"""
import collections
#import random
import heapq
import bisect
import math
import time


class Solution2:
    def solve(self, A1, A2):
        pass


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return b * a // gcd(b, a)


class Solution:

    def solve(self, A, s):
        if sum(A) <= s:
            return 0
        out = 0
        used = 0
        max_seen = 0
        for i, n in enumerate(A):
            if n > max_seen:
                used += max_seen
                max_seen = n
                if used > s:
                    break
                out = i + 1
            else:
                used += n
            if used > s:
                break
        return out


sol = Solution()
sol2 = Solution2()

TT = int(input())
for test_case in range(TT):
    N, K = input().split()
    #s = input()
    #a = []
    # for _ in range(int(N)):
    #a.append([int(c) for c in input().split()])
    b = [int(c) for c in input().split()]

    out = sol.solve(b, int(K))
    print(str(out))
    # print(str(out))

    # out2 = sol2.solve(s)


# for _ in range(100000):
#     rand = [random.randrange(60) for _ in range(10)]
#     out1 = sol.solve(rand)
#     out2 = sol2.solve(rand)
#     if out1 != out2:
#         print(rand, out1, out2)
#         break
