def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def exgcd(a, b):
    if (b == 0):
        return (1, 0, a)
    (p, q, r) = exgcd(b, a % b)
    t = p
    p = q
    q = t - (a // b) * q
    return (p, q, r)
list = input().split()
n = int(list[0]); m = int(list[1]);
x = int(list[2]); y = int(list[3])
vx = int(list[4]); vy = int(list[5])
if (vx == 0):
    if ((x != 0) and (x != n)):
        print(-1)
    else:
        if (vy == 1):
            print(x, m)
        else:
            print(x, 0)
if (vy == 0):
    if ((y != 0) and (y != m)):
        print(-1)
    else:
        if (vx == 1):
            print(n, y)
        else:
            print(0, y)
if ((vx != 0) and (vy != 0)):
    fx = 0; fy = 0
    if (vx == -1):
        fx = 1
        x = n - x
    if (vy == -1):
        fy = 1
        y = m - y
    (p, q, r) = exgcd(n, m)
    if ((x - y) % r != 0):
        print(-1)
    else:
        p *= (x - y) // r
        q *= (x - y) // r
        mn = m * n // gcd(m, n)
        a = (p * n - x) % mn
        while (a <= 0):
            a += mn
        p = (x + a) // n
        q = (y + a) // m
        ansx = 0; ansy = 0;
        if ((p + fx) % 2 == 1):
            ansx = n
        if ((q + fy) % 2 == 1):
            ansy = m
        print(ansx, ansy)

