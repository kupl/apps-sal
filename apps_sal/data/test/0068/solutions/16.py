"""
created by shhuan at 2018/11/3 11:30


search for minimum steps, consider binary search

"""
N = int(input())
ops = [x for x in input()]
(X, Y) = list(map(int, input().split()))
dd = abs(X) + abs(Y)
lops = len(ops)
[ll, lr, lu, ld, rl, rr, ru, rd] = [[0 for _ in range(lops + 2)] for _ in range(8)]
(l, r, u, d) = (0, 0, 0, 0)
for i in range(lops):
    op = ops[i]
    if op == 'L':
        l += 1
    elif op == 'R':
        r += 1
    elif op == 'U':
        u += 1
    else:
        d += 1
    ll[i + 1] = l
    lr[i + 1] = r
    ld[i + 1] = d
    lu[i + 1] = u
(l, r, u, d) = (0, 0, 0, 0)
for i in range(lops - 1, -1, -1):
    op = ops[i]
    if op == 'L':
        l += 1
    elif op == 'R':
        r += 1
    elif op == 'U':
        u += 1
    else:
        d += 1
    rl[i] = l
    rr[i] = r
    rd[i] = d
    ru[i] = u


def check(lsub):
    for i in range(lops - lsub + 1):
        j = i + lsub - 1
        (l0, r0, u0, d0) = (ll[i], lr[i], lu[i], ld[i])
        (l1, r1, u1, d1) = (rl[j + 1], rr[j + 1], ru[j + 1], rd[j + 1])
        x = r0 + r1 - (l0 + l1)
        y = u0 + u1 - (d0 + d1)
        dx = abs(X - x)
        dy = abs(Y - y)
        if dx + dy <= lsub and (lsub - dx - dy) % 2 == 0:
            return True
    return False


(sl, sr) = (0, lops + 1)
while sl < sr:
    m = (sl + sr) // 2
    if check(m):
        sr = m
    else:
        sl = m + 1
sl = -1 if sl > lops else sl
print(sl)
