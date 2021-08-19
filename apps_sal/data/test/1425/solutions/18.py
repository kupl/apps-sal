from collections import deque
n = int(input())
a = list(map(int, input().split()))
a.sort()
d = deque([])
for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        d.append(a[i])
    else:
        d.appendleft(a[i])


def valid(a):
    for i in range(n):
        if a[i - 1] + a[(i + 1) % n] <= a[i]:
            return False
    return True


if valid(d):
    print('YES')
    print(*d)
else:
    print('NO')
