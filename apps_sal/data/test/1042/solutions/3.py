'''
midpow function copy marsi.
39 no line thaki 51 copy marsi.
tou kita oiche
as if i care
'''


import sys
mod = 1000000007


def modpow(a, x):
    if x == 0:
        return 1
    if x == 1:
        return a
    b = modpow(a, x // 2)
    return (b * b * (a ** (x % 2))) % mod


n, m = list(map(int, input().split()))
#ans = gcd(n,m)
if m % n != 0:
    print(0)
    return
if n == m:
    print(1)
    return
ans = m // n
arr = []
i = 2
while i * i < ans:
    if ans % i == 0:
        arr.append(i)
        arr.append(ans // i)
    i += 1
if int(ans ** 0.5) ** 2 == ans:
    arr.append(int(ans ** 0.5))
arr.append(ans)
arr.sort()
result = modpow(2, ans - 1)
muls = [0 for _ in arr]
muls[0] = 1
for xid, d in enumerate(arr):
    prevs = 0
    for id, d2 in enumerate(arr):
        if d2 < d and d % d2 == 0:
            prevs += muls[id]
    muls[xid] = (1 - prevs)
    result += (prevs - 1) * modpow(2, ans // d - 1)

    result = (result + 1000 * mod) % mod
print(result)
