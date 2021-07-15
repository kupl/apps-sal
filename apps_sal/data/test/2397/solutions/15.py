import heapq
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = [0 for i in range(n)]
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]
x = s.pop()
x *= k

heapq.heapify(s)
for _ in range(k - 1):
    x -= heapq.heappop(s)
print(x)


