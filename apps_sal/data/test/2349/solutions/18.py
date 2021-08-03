# from sys import stdin
# def rl():
#     return [int(w) for w in stdin.readline().split()]
from bisect import bisect_right
from bisect import bisect_left
from collections import defaultdict
from math import sqrt, factorial, gcd, log2, inf, ceil
# map(int,input().split())
# # l = list(map(int,input().split()))
# from itertools import permutations
import sys
# input = sys.stdin.readline

# t = int(input())
#
# for _ in range(t):
#     a,b,c = map(int,input().split())
#     a,b,c = sorted([a,b,c])
#     ans = 0
#     ans+=b
#     c-=b
#
#     a,c = sorted([a,c])
#     ans+=a
#     print(ans)


# print(ans)


t = int(input())

for _ in range(t):

    n = int(input())

    ans = [1, 0]

    for i in range(1, int(sqrt(n) + 1)):
        ans.append(n // i)
        ans.append(n // (n // i))

    ans = list(set(ans))
    print(len(ans))
    ans.sort()
    print(*ans)
