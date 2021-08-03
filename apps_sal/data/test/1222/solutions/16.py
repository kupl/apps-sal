from collections import deque

k = int(input())
d = deque()
for i in range(1, 10):
    d.append(i)

for i in range(1, k):
    v = d.popleft()
    s = v % 10
    if s > 0:
        d.append(10 * v + s - 1)
    d.append(10 * v + s)
    if s < 9:
        d.append(10 * v + s + 1)

print(d[0])
