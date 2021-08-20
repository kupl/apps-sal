(x, n) = map(int, input().split())
mod = 1000000007
res = 1


def bpow(x, y):
    res = 1
    while y > 0:
        if y % 2 == 1:
            res = res * x % mod
            y -= 1
        else:
            x = x * x % mod
            y //= 2
    return res


sp = []
i = 2
while i * i <= x:
    if x % i == 0:
        sp.append(i)
        while x % i == 0:
            x //= i
    i += 1
if x > 1:
    sp.append(x)
for i in sp:
    st = 1
    while st <= n:
        st *= i
    st //= i
    byv = 0
    while st > 0:
        cnk = n // st
        cnk -= byv
        res = res * bpow(st, cnk) % mod
        byv += cnk
        st //= i
print(res)
