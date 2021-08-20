import heapq
s = []
(n, k) = list(map(int, input().split()))
for _ in range(n):
    (t, b) = list(map(int, input().split()))
    s.append((t, b))
s.sort(key=lambda x: x[1], reverse=True)
t_max = t = s[0][0] * s[0][1]
i = 1
while i < k:
    t = (t // s[i - 1][1] + s[i][0]) * s[i][1]
    if t > t_max:
        t_max = t
    i += 1
h = [x[0] for x in s[:k]]
heapq.heapify(h)
for i in range(1, n - k + 1):
    sm = heapq.heappushpop(h, s[i + k - 1][0])
    t = (t // s[i - 2 + k][1] - sm + s[i + k - 1][0]) * s[i + k - 1][1]
    if t > t_max:
        t_max = t
print(t_max)
