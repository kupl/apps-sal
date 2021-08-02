from heapq import *
n = int(input())
a = list(map(int, input().split()))

left = a[:n]
right = a[2 * n:]
heapify(left)
l = [sum(left)]
r = [sum(right)]
sl = sum(left)
sr = sum(right)
for i in range(n):
    k = heappop(left)
    sl -= k
    heappush(left, max(k, a[n + i]))
    sl += max(k, a[n + i])
    l.append(sl)

right = [-i for i in right]
heapify(right)
for i in range(n):
    k = -heappop(right)
    sr -= k
    mini = min(k, a[2 * n - 1 - i])
    heappush(right, -mini)
    sr += mini
    r.append(sr)

r.reverse()
ans = -10**15
for i in range(n + 1):
    ans = max(l[i] - r[i], ans)

print(ans)
