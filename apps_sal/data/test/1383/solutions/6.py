import sys
import math
input = sys.stdin.readline
(n, m) = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
alist.sort()
blist.sort()
minx = math.inf
for i in range(n):
    diff = (blist[0] - alist[i] + m) % m
    arr = []
    for j in range(n):
        arr.append((alist[j] + diff) % m)
    arr.sort()
    flag = True
    for j in range(n):
        if arr[j] != blist[j]:
            flag = False
            break
    if flag:
        minx = min(minx, diff)
print(minx)
