n = int(input())
curpow, t, mx2pow = 1, 1, 0
while t < n:
    t <<= 1
    mx2pow += 1

if t > n:
    mx2pow -= 1

last = 1 << (mx2pow - 1) if mx2pow else 1
add = last

while last < n:
    last += add

if last > n:
    last -= add

while n:
    if n == 1:
        print(last)
        break
    print((str(curpow) + ' ') * ((n + 1) // 2), end='')
    curpow *= 2
    n //= 2
