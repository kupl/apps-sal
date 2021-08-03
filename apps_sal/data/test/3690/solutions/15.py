h, m, s, t1, t2 = list(map(int, input().split()))
m += s / 60
h += m / 60
h %= 12
t1, t2 = min(t1, t2), max(t1, t2)
if ((t1 <= h <= t2) and (t1 <= m / 5 <= t2) and (t1 <= s / 5 <= t2)) or \
        (not (t1 <= h <= t2) and not (t1 <= m / 5 <= t2) and not (t1 <= s / 5 <= t2)):
    print('YES')
else:
    print('NO')
