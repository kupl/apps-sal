import math

(n, m, q) = input().split()
n = int(n)
m = int(m)
q = int(q)

gcd = math.gcd(n, m)
lcm = n * m // gcd
block = lcm // gcd
for i in range(q):
    a, b, c, d = input().split()

    a = int(a)
    b = int(b)
    pa = 0
    pb = 0

    if a == 1:
        pa = lcm // n * b
    else:
        pa = lcm // m * b

    c = int(c)
    d = int(d)
    if c == 1:
        pb = lcm // n * d
    else:
        pb = lcm // m * d

    if (pa - 1) // block == (pb - 1) // block:
        print("YES")
    else:
        print("NO")
