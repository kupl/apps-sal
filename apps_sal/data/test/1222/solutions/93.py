from collections import deque
k = int(input())
q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(k):
    a = q.popleft()
    b = a % 10
    if b == 0:
        q.append(a * 10)
        q.append(a * 10 + b + 1)
    elif b == 9:
        q.append(a * 10 + b - 1)
        q.append(a * 10 + b)
    else:
        q.append(a * 10 + b - 1)
        q.append(a * 10 + b)
        q.append(a * 10 + b + 1)
print(a)
