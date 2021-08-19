def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


n = int(input())
(a, b) = (n // 2, n // 2 + n % 2)
while gcd(a, b) > 1:
    a -= 1
    b += 1
print(a, b)
