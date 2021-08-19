import sys


def rs():
    return sys.stdin.readline().rstrip()


def ri():
    return int(rs())


def rs_():
    return [_ for _ in rs().split()]


def ri_():
    return [int(_) for _ in rs().split()]


N = ri()
c = list(rs())
ans = 0
s = 0
e = N - 1
while True:
    while c[s] == 'R' and s < e:
        s += 1
    while c[e] == 'W' and s < e:
        e -= 1
    if s == e:
        break
    else:
        c[s] = 'R'
        c[e] = 'W'
        ans += 1
print(ans)
