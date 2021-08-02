

import sys
mod = 1000000007


def modpow(a, x):
    if x == 0:
        return 1
    if x == 1:
        return a
    b = modpow(a, x // 2)
    return (b * b * (a ** (x % 2))) % mod


x, y = list(map(int, input().split()))
if y % x != 0:
    print(0)
    return
if x == y:
    print(1)
    return

a = y // x

divs = []

i = 2
while i * i < a:
    if a % i == 0:
        divs.append(i)
        divs.append(a // i)
    i += 1

if int(a ** 0.5) ** 2 == a:
    divs.append(int(a**0.5))

divs.append(a)

divs.sort()

# print(divs)

res = modpow(2, a - 1)
muls = [0 for _ in divs]
muls[0] = 1

for xid, d in enumerate(divs):
    prevs = 0
    for id, d2 in enumerate(divs):
        if d2 < d and d % d2 == 0:
            prevs += muls[id]
    muls[xid] = (1 - prevs)
    res += (prevs - 1) * modpow(2, a // d - 1)

    res = (res + 1000 * mod) % mod
    #print(d, res, ',', prevs)

# print(muls)
print(res)
