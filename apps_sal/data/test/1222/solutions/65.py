from collections import deque

K = int(input())

d = deque(i for i in range(1, 10))

count = 0

while count != K:
    x = d.popleft()
    a = (10 * x) + (x % 10)
    if x % 10 != 0:
        d.append(a - 1)

    d.append(a)

    if x % 10 != 9:
        d.append(a + 1)

    count += 1

print(x)
