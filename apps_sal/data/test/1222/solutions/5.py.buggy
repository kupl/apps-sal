from collections import deque
k = int(input())

q = deque()
for i in range(1, 10):
    q.append(i)
cnt = 0
while True:
    a = q.popleft()
    cnt += 1
    if cnt == k:
        print(a)
        return
    b = a % 10
    for i in (-1, 0, 1):
        if 0 <= b + i <= 9:
            q.append(a * 10 + b + i)
