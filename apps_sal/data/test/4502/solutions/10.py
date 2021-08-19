from collections import deque
b = deque()
n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
    if i % 2 == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])
b = list(b)
if n % 2 == 1:
    b = b[::-1]
b = [str(i) for i in b]
print(' '.join(b))
