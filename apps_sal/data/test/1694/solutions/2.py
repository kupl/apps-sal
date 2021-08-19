(n, m, s, f) = [int(x) for x in input().split()]
now = 1
d = 1 if f > s else -1
step = 'R' if d == 1 else 'L'
ret = ''
for _ in range(m):
    (t, l, r) = [int(x) for x in input().split()]
    if t > now:
        flag = False
        while t > now:
            s += d
            ret += step
            now += 1
            if s == f:
                flag = True
                break
        if flag:
            break
    if l <= s <= r or l <= s + d <= r:
        ret += 'X'
    else:
        ret += step
        s += d
    if s == f:
        break
    now += 1
while s != f:
    s += d
    ret += step
print(ret)
