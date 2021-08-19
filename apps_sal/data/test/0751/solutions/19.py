from collections import deque
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
(in_bus, left) = (0, 0)
groups = deque(a)
while groups:
    if in_bus + groups[0] <= m:
        in_bus += groups[0]
        if in_bus == m:
            left += 1
            in_bus = 0
        groups.popleft()
    else:
        left += 1
        in_bus = 0
if in_bus:
    left += 1
print(left)
