from collections import deque
K = int(input())
count = 0
todo = deque(range(1, 10))
while todo:
    x = todo.popleft()
    count += 1
    if count == K:
        print(x)
        break
    i = x % 10
    if 0 < i:
        todo.append(x * 10 + i - 1)
    todo.append(x * 10 + i)
    if i < 9:
        todo.append(x * 10 + i + 1)
