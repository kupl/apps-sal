from collections import deque

k = int(input())

lunlun = deque(i for i in range(1, 10))
for _ in range(k - 1):
    p = lunlun.popleft()
    if p % 10 != 0:
        lunlun.append(10 * p + p % 10 - 1)
    lunlun.append(10 * p + p % 10)
    if p % 10 != 9:
        lunlun.append(10 * p + p % 10 + 1)
print(lunlun.popleft())
