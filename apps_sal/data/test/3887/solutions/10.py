(sgn, a, b) = (1, 0, 0)
sol = ''
ok = 0
for ch in input().split():
    if ch == '?':
        if sgn == 1:
            a += 1
            ch = 'P'
        else:
            b += 1
            ch = 'M'
    elif ch == '+':
        sgn = 1
    elif ch == '-':
        sgn = -1
    elif ch != '=':
        n = int(ch)
        ok = 1
    if not ok:
        sol += ch
(pl, mn) = ([n] * a, [1] * b)
s = n * a - b
(i, j) = (0, 0)
while s > n and (i < a or j < b):
    if i < a:
        amt = min(s - n, n - 1)
        pl[i] -= amt
        s -= amt
        i += 1
    else:
        amt = min(s - n, n - 1)
        mn[j] += amt
        s -= amt
        j += 1
if s != n:
    print('Impossible')
else:
    print('Possible')
    for ch in sol:
        if ch != 'P' and ch != 'M':
            print(ch, end=' ')
        elif ch == 'P':
            print(pl[-1], end=' ')
            pl.pop()
        else:
            print(mn[-1], end=' ')
            mn.pop()
    print(n)
