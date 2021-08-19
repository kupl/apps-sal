def check(x):
    if x % 2 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d += 2
    return True


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('FastestFinger')
        continue
    if n == 2:
        print('Ashishgup')
        continue
    p2 = 0
    while n % 2 == 0:
        n //= 2
        p2 += 1
    if n == 1:
        print('FastestFinger')
    elif p2 != 1:
        print('Ashishgup')
    elif check(n):
        print('FastestFinger')
    else:
        print('Ashishgup')
