def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = map(int, input().split())

tmp = gcd(a, b)
print(int(a * b / tmp))
