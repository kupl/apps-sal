import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")


s = input()
idxs = [[] for i in range(26)]


def wid(w):
    return ord(w) - ord("a")


for i in range(len(s)):
    w = s[i]
    idxs[wid(w)].append(i)
a = -1
b = -1
for i in range(26):
    if len(idxs[i]) >= 2:
        prev = idxs[i][0]
        for nex in idxs[i]:
            d = nex - prev
            if 1 <= d <= 2:
                a = prev + 1
                b = nex + 1
                break
            prev = nex
print(a, b)
