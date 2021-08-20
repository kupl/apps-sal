from collections import deque
n = int(input())
a = list(input().split())
q = deque()
for i in range(n):
    if n & 1:
        if i & 1:
            q.append(a[i])
        else:
            q.appendleft(a[i])
    elif i & 1:
        q.appendleft(a[i])
    else:
        q.append(a[i])
for i in q:
    print(i, end=' ')
