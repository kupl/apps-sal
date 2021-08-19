from collections import deque

k = int(input())

# [1, 2, 3, 4, .. 9]
que = deque([i for i in range(1, 10, 1)])

for i in range(k):
    # smollest elements in que
    x = que.popleft()

    # 0's next must be 1 or 0
    if x % 10 == 0:
        que.append(x * 10)
        que.append(x * 10 + 1)
    # 9's next must be 8 or 9
    elif x % 10 == 9:
        que.append(x * 10 + 8)
        que.append(x * 10 + 9)
    # others are remain or remain-1 or remain+1
    else:
        que.append(x * 10 + x % 10 - 1)
        que.append(x * 10 + x % 10)
        que.append(x * 10 + x % 10 + 1)

print(x)
