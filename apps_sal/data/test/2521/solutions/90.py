import heapq
n = int(input())
a = list(map(int, input().split()))
h = a[:n]
heapq.heapify(h)
first = [0] * (n + 1)
s = sum(a[:n])
first[0] = s
for i in range(n):
    s += a[n + i]
    heapq.heappush(h, a[n + i])
    s -= heapq.heappop(h)
    first[i + 1] = s
h = list(map(lambda x: -x, a[2 * n:]))
heapq.heapify(h)
second = [0] * (n + 1)
s = -sum(a[2 * n:])
second[0] = s
for i in range(n):
    s -= a[2 * n - i - 1]
    heapq.heappush(h, -a[2 * n - i - 1])
    s -= heapq.heappop(h)
    second[i + 1] = s
ans = -10 ** 18
for i in range(n + 1):
    ans = max(ans, first[i] + second[n - i])
print(ans)
