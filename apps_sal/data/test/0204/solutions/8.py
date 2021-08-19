def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


(a, b, x, y) = map(int, input().split())
k = gcd(x, y)
x //= k
y //= k
print(min(a // x, b // y))
