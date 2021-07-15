def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b, c = list(map(int, input().split()))
print(c // ((a * b) // gcd(a, b)))

