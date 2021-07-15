def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)

def works(a, b, c, d, x):
    return b <= d * x and a <= c * x and d * x - b >= c * x - a

def solve():
    a, b, c, d = list(map(int, input().rstrip().split()))
    if c == d == 1 and not a / b == 1:
        print(-1)
        return
    if c == 0 and not a == 0:
        print(-1)
        return
    g = gcd(c, d)
    c //= g
    d //= g
    low = -1
    high = 1000000000000
    while low + 1 < high:
        mid = (low + high) // 2
        if works(a, b, c, d, mid):
            high = mid
        else:
            low = mid
    print(d * high - b)

def __starting_point():
    t = int(input())
    for _ in range(t):
        solve()

__starting_point()
