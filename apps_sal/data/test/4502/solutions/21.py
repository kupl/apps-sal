from collections import deque
n = int(input())
a = deque(list(map(int, input().split())))
b = deque() if n % 2 == 0 else deque([a.popleft()])
for _ in range(n // 2):
    b.append(a.popleft())
    b.appendleft(a.popleft())
print(*b)
