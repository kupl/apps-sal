# ls.sort(key=lambda x: (x[0], x[1]))
from bisect import bisect_left
import sys

inf = float("inf")
mod = 1000000007


def array(): return list(map(int, sys.stdin.readline().split()))
def intt(): return list(map(int, sys.stdin.readline().split()))


#n, k = map(int, sys.stdin.readline().split())
#arr = list(map(int, sys.stdin.readline().split()))
#arr=[(int(x),i) for i,x in enumerate(input().split())]
# ls=list(map(int,input().split()))
# for i in range(m):
# print(s[i],end="")
# n=int(sys.stdin.readline())
n, m, k = list(map(int, sys.stdin.readline().split()))
ls = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    ls.append(arr)
print(m * (m - 1) // 2)
for i in range(1, m):
    for j in range(i + 1, m + 1):
        if k == 0:
            print(i, j)
        else:
            print(j, i)
