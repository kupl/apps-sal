(n, m, s, f) = map(int, input().split())
t = dict()
for i in range(m):
    (t1, l1, r1) = map(int, input().split())
    t[t1] = (l1, r1)
pos = s
i = 1
while 1:
    if pos == f:
        break
    if i in t:
        if t[i][0] <= pos <= t[i][1]:
            print('X', end='')
            i += 1
            continue
        elif f - pos > 0 and t[i][0] <= pos + 1 <= t[i][1]:
            print('X', end='')
            i += 1
            continue
        elif f - pos < 0 and t[i][0] <= pos - 1 <= t[i][1]:
            print('X', end='')
            i += 1
            continue
    if f - pos > 0:
        print('R', end='')
        pos += 1
    elif pos - f > 0:
        print('L', end='')
        pos -= 1
    i += 1
