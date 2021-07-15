def nok(a, b):
    return (a * b) // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def test(z):
    nonlocal x, a, y, b, p, k
    ans = 0
    xayb = z // nok(a, b)
    xa = z // a - xayb
    yb = z // b - xayb
    if x >= y:
        x1 = xa
        x2 = yb
        y1 = x
        y2 = y
    else:
        x1 = yb
        x2 = xa
        y1 = y
        y2 = x
    for i in range(xayb):
        ans += (p[i] // 100) * (x + y)
    for i in range(xayb, xayb + x1):
        ans += (p[i] // 100) * y1
    for i in range(xayb + x1, xayb + x1 + x2):
        ans += (p[i] // 100) * y2
    return ans >= k

q = int(input())
for i in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    p.sort(reverse = True)
    x, a = map(int, input().split())
    y, b = map(int, input().split())
    k = int(input())
    left = 0
    right = n
    if not test(right):
        print(-1)
    else:
        while right - left > 1:
            mid = (left + right) // 2
            if test(mid):
                right = mid
            else:
                left = mid
        print(right)
