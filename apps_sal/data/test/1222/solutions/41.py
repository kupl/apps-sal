from collections import deque
D = deque()
for i in range(1, 10):
    D.append(i)
for _ in range(int(input())):
    x = D.popleft()
    y = x % 10
    if y != 0:
        D.append(10 * x + y - 1)
    D.append(10 * x + y)
    if y != 9:
        D.append(10 * x + y + 1)
print(x)

