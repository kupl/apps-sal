n = int(input())
some_pow = False
prime = True
d = 2
while d * d <= n:
    if n % d == 0:
        tst = n
        while tst % d == 0 and tst > 1:
            tst //= d
        if tst == 1:
            some_pow = True
        prime = False
        break
    d += 1
if prime:
    print(n)
elif some_pow:
    print(d)
else:
    print(1)

