from collections import deque

N = int(input())

Q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(N - 1):
    x = Q.popleft()
    if x % 10 != 0:
        y = 10 * x + x % 10 - 1
        Q.append(y)

    y = 10 * x + x % 10
    Q.append(y)

    if x % 10 != 9:
        y = 10 * x + x % 10 + 1
        Q.append(y)

ans = Q.popleft()

print(ans)
