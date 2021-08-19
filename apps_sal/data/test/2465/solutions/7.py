def compute_gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


T = int(input())
while T:
    x = int(input())
    gcd = compute_gcd(180, x)
    if 180 % gcd > 0:
        print(-1)
    else:
        n = int(180 / gcd)
        if n * gcd == 180:
            y = x * n / 180
            if y == n - 1:
                n = 2 * n
        else:
            n = -1
        print(n)
    T -= 1
