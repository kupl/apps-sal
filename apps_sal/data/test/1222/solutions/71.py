from collections import deque

K = int(input())
d = deque()

for i in range(1, 10):
    d.append(i)

for i in range(1, K):
    s = d.popleft()
    v = s % 10
    if v > 0:
        d.append(10 * s + v - 1)
    d.append(10 * s + v)
    if v < 9:
        d.append(10 * s + v + 1)
print((d.popleft()))
