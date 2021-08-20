from collections import deque
(n, a, b) = (int(input()), deque(map(int, input().split())), deque())
for i in range(n):
    if n % 2 == 0:
        if i % 2 == 0:
            b.append(a[i])
        else:
            b.appendleft(a[i])
    elif i % 2 == 0:
        b.appendleft(a[i])
    else:
        b.append(a[i])
print(*b, sep=' ')
