def AC():
    a, b, p, x = map(int, input().split())
    ans = 0
    m = 1
    for i in range(p - 2):
        m = (m * a) % p
    rem = 1
    inv = 1
    Ch = p * (p - 1)
    for n in range(1, p):
        rem = (rem * a) % p
        inv = (inv * m) % p
        cur = min(p, ((n * rem - b) * inv + p) % p)
        rep = n + cur * (p - 1)
        ans += max(0, (x - rep + Ch) // Ch)
    print(ans)
AC()
