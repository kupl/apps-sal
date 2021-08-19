from collections import deque
with open(0) as f:
    (n, *a) = map(int, f.read().split())
b = deque()
for (idx, value) in enumerate(a):
    if idx & 1 ^ n & 1:
        b.appendleft(value)
    else:
        b.append(value)
print(*b)
