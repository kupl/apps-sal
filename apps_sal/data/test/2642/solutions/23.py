from math import gcd

n = int(input())
ration = dict()
used = dict()
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a == 0 or b == 0:
        if a == b == 0:
            r = '0'
        elif a == 0:
            r = '0a'
        else:
            r = '0b'
    else:
        s = '-' if (a < 0) ^ (b < 0) else '+'
        a = abs(a)
        b = abs(b)
        g = gcd(a, b)
        r = f'{s} {a//g} {b//g}'
    ration[r] = ration.get(r, 0) + 1
    used[r] = 0

res = 1
mod = 10**9 + 7
add = 0
for k, v in list(ration.items()):
    if used[k]:
        continue
    if k == '0':
        add += v
        used[k] = 1
    elif k == '0a' or k == '0b':
        res *= 2**ration.get('0a', 0) + 2**ration.get('0b', 0) - 1
        used['0a'] = used['0b'] = 1
    else:
        r = k.split()
        l = f'{"-" if r[0]=="+" else "+"} {r[2]} {r[1]}'
        res *= 2**v + 2**ration.get(l, 0) - 1
        used[k] = used[l] = 1
    res %= mod

res += add
res -= 1
if res < 0:
    res += mod
print(res)
