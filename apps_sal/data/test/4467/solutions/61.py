import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("YES") if fl else print("NO")


n = ni()
ab = []
for i in range(n):
    ab.append(lma())
ab.sort(key=lambda x: x[1], reverse=True)
ab.sort(reverse=True)
cd = []
for i in range(n):
    cd.append(lma())
cd.sort()
cd.sort(key=lambda x: x[1])
cnt = 0
INF = 10**9
for a, b in ab:
    # print("ab",a,b)
    for i in range(n):
        c, d = cd[i]
        if a < c and b < d:
            # print("cd",c,d)
            cnt += 1
            cd[i][0] = -INF
            cd[i][1] = -INF
            break
print(cnt)
# print(cd)
