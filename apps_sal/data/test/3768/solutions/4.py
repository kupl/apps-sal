def gcd(m, n):
    if m < n:
        m, n = n, m
    r = m % n
    while r:
        m, n = n, r
        r = m % n
    return n

def search(x, y):
    nonlocal ans
    while True:
        if x == 1:
            ans = ans + ("" if y == 1 else str(y - 1) + 'B')
            return
        if y == 1:
            ans = ans + ("" if x == 1 else str(x - 1) + 'A')
            return
        if x < y:
            ans = ans + str(y // x) + 'B'
            x, y = x, y % x
        else:
            ans = ans + str(x // y) + 'A'
            x, y = x % y, y

a, b = [ int(i) for i in input().split() ]

if gcd(a, b) != 1:
    print("Impossible")
else:
    ans = ""
    search(a, b)
    print(ans)
