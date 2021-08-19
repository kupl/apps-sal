def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
a = (n - 1) // 2
while gcd(a, n - a) != 1:
    a -= 1
print(a, n - a)
