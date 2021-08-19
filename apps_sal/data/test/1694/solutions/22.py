(n, m, s, f) = map(int, input().split())
q = dict()
for i in range(m):
    (t, l, r) = map(int, input().split())
    q[t] = (l, r)
k = 1
pos = s
while pos != f:
    if k in q:
        if q[k][0] <= pos <= q[k][1]:
            print('X', end='')
        elif 1 < pos < n:
            if pos > f:
                if q[k][0] <= pos - 1 <= q[k][1]:
                    print('X', end='')
                else:
                    print('L', end='')
                    pos -= 1
            elif q[k][0] <= pos + 1 <= q[k][1]:
                print('X', end='')
            else:
                print('R', end='')
                pos += 1
        elif pos == 1:
            if q[k][0] <= 2 <= q[k][1]:
                print('X', end='')
            else:
                print('R', end='')
                pos = 2
        elif pos == n:
            if q[k][0] <= pos - 1 <= q[k][1]:
                print('X', end='')
            else:
                print('L', end='')
                pos -= 1
    elif pos > f:
        print('L', end='')
        pos -= 1
    else:
        print('R', end='')
        pos += 1
    k += 1
