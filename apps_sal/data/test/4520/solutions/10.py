import sys
from collections import deque
readline = sys.stdin.readline

n, k = map(int, readline().split())

tmp = []
for i in range(n):
    a, b = map(int, readline().split())
    tmp.append([b, a, i])
tmp.sort()
ans = []
for i in range(201):
    s = 0
    asd = []
    for x in tmp:
        if i <= x[0] and i >= x[1]:
            s += 1
            if s > k:
                ans.append(x[2] + 1)
                asd.append(x)
    for x in asd:
        tmp.remove(x)
print(len(ans))
for x in ans:
    print(x, end=' ')
