import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = [-int(input()) for _ in range(N)]

from bisect import bisect_right
lis = [1]
for a in As:
    if a>=lis[-1]:
        lis.append(a)
    else:
        lis[bisect_right(lis, a)] = a

print(len(lis))
