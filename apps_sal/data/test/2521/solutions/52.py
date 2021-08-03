from heapq import heappop, heappush
n = int(input())
a = list(map(int, input().split()))
p = sum(a[2 * n:])
right_min = [p]
hq = []
for i in range(2 * n, 2 * n + n):
    heappush(hq, -a[i])
for i in range(n):
    p += a[-n - i - 1]
    heappush(hq, -a[-n - i - 1])
    p += heappop(hq)
    right_min.append(p)
l = sum(a[:n])
hq = []
for i in range(n):
    heappush(hq, a[i])
right_min.reverse()
ans = l - right_min[0]
for i in range(n):
    l += a[n + i]
    heappush(hq, a[n + i])
    l -= heappop(hq)
    ans = max(ans, l - right_min[i + 1])
print(ans)
