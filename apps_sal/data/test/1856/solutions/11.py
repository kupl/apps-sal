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
input = sys.stdin.readline

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

def find_parent(u):
    if par[u] != u:
        par[u] = find_parent(par[u])
    return par[u]


n = int(input())
la = []

hash = defaultdict(list)
par = [0] + [i + 1 for i in range(26)]
rank = [1] * (26 + 1)
seti = set()
booli = [False] * (27)
for i in range(n):
    z = input()

    z = z[:len(z) - 1]
    k = min(z)

    set1 = set(min(k))

    booli[ord(k) - 97 + 1] = True

    a = ord(k) - 97 + 1
    z2 = find_parent(a)
    for i in range(len(z)):
        booli[ord(z[i]) - 97 + 1] = True

        if z[i] not in set1:

            b = ord(z[i]) - 97 + 1
            z1 = find_parent(b)
            if z1 != z2:
                par[z1] = z2

            set1.add(i)

ans = set()

for i in range(26):
    if booli[i + 1] == True:
        # print(chr(i+98))
        z = find_parent(i + 1)
        ans.add(z)

print(len(ans))
