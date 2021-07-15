
from collections import deque

k = int(input())
q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

if k <= 9:
    print(q[k-1])
    return

i = 9
while 1:
    a = q.popleft()
    b = a % 10
    if b == 0:
        q.append(a * 10)
        i += 1
        if i == k:
            print(q[-1])
            return
        q.append(a * 10 + b + 1)
        i += 1
        if i == k:
            print(q[-1])
            return
    elif b == 9:
        q.append(a * 10 + b - 1)
        i += 1
        if i == k:
            print(q[-1])
            return
        q.append(a * 10 + b)
        i += 1
        if i == k:
            print(q[-1])
            return
    else:
        q.append(a * 10 + b - 1)
        i += 1
        if i == k:
            print(q[-1])
            return
        q.append(a * 10 + b)
        i += 1
        if i == k:
            print(q[-1])
            return
        q.append(a * 10 + b + 1)
        i += 1
        if i == k:
            print(q[-1])
            return
