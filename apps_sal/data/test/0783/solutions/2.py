import sys


n = int(input())
h = [int(i) for i in input().split()]
h = h[::-1]
ans = []
curmax = h[0] - 1
for i in range(n):
    if h[i] <= curmax:
        ans.append(curmax + 1 - h[i])
    else:
        ans.append(0)
    curmax = max(curmax, h[i])

ans = ans[::-1]
for x in ans:
    print(x, end=' ')
