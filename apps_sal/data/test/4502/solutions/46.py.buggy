from collections import deque

n = int(input())
a = list(map(int, input().split()))

d = deque()
for i in range(n):
    if n % 2 == (i + 1) % 2:
        d.appendleft(a[i])
    else:
        d.append(a[i])

print((*d))
