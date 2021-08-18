from sys import stdin, stdout
from collections import defaultdict
import math
I = stdin.readline
P = stdout.write

n, m = map(int, I().split())
arr = [int(x) for x in I().split()]

indi = defaultdict(lambda: set())
for j in range(m):
    l, r = map(int, I().split())
    for i in range(l - 1, r):

        indi[i].add(j + 1)

ans = 0
a, b = 0, 0
inter = set()
for i in range(n):
    for j in range(n):
        nowint = indi[j].intersection(indi[i])
        now = arr[i] - arr[j] + len(indi[j]) - len(nowint)

        if(now > ans):
            ans = now
            a = i
            b = j
            inter = nowint

print(ans)
print(len(indi[b]))
for i in indi[b]:

    print(i, end=" ")
