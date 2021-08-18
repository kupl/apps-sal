from collections import deque

k = int(input())

que = deque([i for i in range(1, 10, 1)])

for i in range(k):
    x = que.popleft()

    if x % 10 == 0:
        que.append(x * 10)
        que.append(x * 10 + 1)
    elif x % 10 == 9:
        que.append(x * 10 + 8)
        que.append(x * 10 + 9)
    else:
        que.append(x * 10 + x % 10 - 1)
        que.append(x * 10 + x % 10)
        que.append(x * 10 + x % 10 + 1)

print(x)
