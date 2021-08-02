from collections import deque as D
t = int(input())
for _ in range(t):
    a = D(list(input()))
    b = D(list(input()))
    p = None
    f = True
    while a and b:
        x = a.popleft()
        if b[0] == x:
            b.popleft()
        elif b[0] == p:
            while b and b[0] == p:
                b.popleft()
            if not b:
                f = False
                break
            if b[0] == x:
                b.popleft()
            else:
                f = False
        else:
            f = False
        p = x
    if a:
        f = False
    if b and set(b) != {p}:
        f = False
    if f:
        print('YES')
    else:
        print('NO')
