
from collections import deque

a = deque(list(range(1, 10)))
for _ in range(int(input())):
    i = a.popleft()
    m = i % 10
    i = 10 * i + m
    if m > 0:
        a.append(i - 1)
    a.append(i)
    if m < 9:
        a.append(i + 1)
print((i // 10))
