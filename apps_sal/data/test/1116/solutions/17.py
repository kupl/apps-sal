def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(input())
for _ in range(t):
    (a, b, k) = map(int, input().split())
    if a > b:
        (a, b) = (b, a)
    gcd_ab = gcd(a, b)
    tmp = a % gcd_ab + gcd_ab
    if -(-(b - tmp) // a) < k:
        print('OBEY')
    else:
        print('REBEL')
