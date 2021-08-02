import heapq
n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))
d = []
s = 0
for i in range(n):
    ans = 0
    heapq.heappush(d, v[i] + s)
    while d and d[0] <= s + t[i]:
        ans += d[0] - s
        heapq.heappop(d)
    s += t[i]
    ans += len(d) * t[i]
    print(ans, end=' ')
