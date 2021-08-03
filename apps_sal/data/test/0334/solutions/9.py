from fractions import gcd

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

# ax+b=cy+d

val = gcd(a, c)

if (d - b) % val != 0:
    print(-1)
else:
    i = b
    while True:
        if ((i - d) % c == 0) and (i - d) / c >= 0:
            break
        i = i + a
    print(i)
