import queue
q = queue.PriorityQueue()
(n, m, r, k) = map(int, input().split())
a = min(r, n - r + 1)
b = min(r, m - r + 1)
u = n - 2 * a + 2
v = m - 2 * b + 2
for i in range(1, a + 1):
    q.put((-b * i, i))
t = 0
while k:
    (s, i) = q.get()
    q.put((s + i, i))
    d = min((u if i == a else 2) * (v if s == -b * i else 2), k)
    t -= s * d
    k -= d
print(t / (n - r + 1) / (m - r + 1))
