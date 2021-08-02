def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


n, m, k = [int(i) for i in input().split()]
if ((2 * n * m) % k != 0):
    print("NO")
else:
    print("YES")
    newk = k / gcd(2 * n, k)
    a = n / gcd(2 * n, k)
    b = m / newk

    if (2 * a <= n):
        a = a * 2
    else:
        b = b * 2

    a = int(a)
    b = int(b)
    print(0, 0)
    print(a, 0)
    print(0, b)
