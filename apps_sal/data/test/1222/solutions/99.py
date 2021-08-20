from collections import deque
K = int(input())
lunlun = deque([i for i in range(1, 10)])
for i in range(K):
    x = lunlun.popleft()
    if x % 10 != 0:
        lunlun.append(x * 10 + x % 10 - 1)
    lunlun.append(x * 10 + x % 10)
    if x % 10 != 9:
        lunlun.append(x * 10 + x % 10 + 1)
print(x)
