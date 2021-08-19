def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for i in ' ' * int(input()):
    (r, b, k) = map(int, input().split())
    g = gcd(r, b)
    r /= g
    b /= g
    if r > b:
        (r, b) = (b, r)
    if r == 1:
        if b > k:
            print('REBEL')
        else:
            print('OBEY')
    elif r * (k - 1) + 1 <= b - 1:
        print('REBEL')
    else:
        print('OBEY')
