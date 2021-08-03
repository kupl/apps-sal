from collections import deque
K = int(input())

q = deque(list(range(1, 10)))

ans = 0
num = 0
for i in range(K):
    num = q.popleft()
    ans = num
    if num % 10 != 0:
        q.append(num * 10 + (num % 10 - 1))
    q.append(num * 10 + num % 10)
    if num % 10 != 9:
        q.append(num * 10 + (num % 10 + 1))

print(ans)
