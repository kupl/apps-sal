def gcd(a, b):
    if(a % b == 0):
        return b
    return gcd(b, a % b)


a, b, c, d = list(map(int, input().split()))

a *= c * d
b *= c * d

if a / c * d <= b:
    a = b - a / c * d
    g = gcd(a, b)
    print(str(int(a / g)) + '/' + str(int(b / g)))

else:
    b = a - b / d * c
    g = gcd(a, b)
    print(str(int(b / g)) + '/' + str(int(a / g)))
