mod = int(1000000000.0 + 7)
k = int(input())
top = 1
yoink = 1
a = list(map(int, input().split()))
for thing in a:
    top *= thing
    yoink *= thing
    yoink %= 2
    top %= mod - 1


def extended_gcd(aa, bb):
    (lastremainder, remainder) = (abs(aa), abs(bb))
    (x, lastx, y, lasty) = (0, 1, 1, 0)
    while remainder:
        (lastremainder, (quotient, remainder)) = (remainder, divmod(lastremainder, remainder))
        (x, lastx) = (lastx - quotient * x, x)
        (y, lasty) = (lasty - quotient * y, y)
    return (lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1))


def modinv(a, m):
    (g, x, y) = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


if top == 0:
    bot = modinv(2, mod)
else:
    bot = pow(2, top - 1, mod)
if yoink % 2 == 0:
    blah = modinv(3, mod)
    blah *= bot + 1
    blah %= mod
    print(str(blah) + '/' + str(bot))
else:
    blah = modinv(3, mod)
    blah *= bot + 2
    blah %= mod
    print(str(blah - 1) + '/' + str(bot))
