def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


t = int(input())
for i in range(t):
    ang = int(input())
    g = gcd(ang, 180)
    k = (2 * g + 180 - ang - 1) // (180 - ang)
    print(180 // g * k)
