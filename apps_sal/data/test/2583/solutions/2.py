def cf(x):
    for i in range(3, x):
        if i ** 2 > x:
            return False
        if x % i == 0:
            return True
    return False


def solve():
    n = int(input())
    if n == 1:
        print('FastestFinger')
        return
    if n == 2:
        print('Ashishgup')
        return
    if n % 2 == 0:
        if n // 2 % 2 == 1:
            if cf(n // 2):
                print('Ashishgup')
            else:
                print('FastestFinger')
            return
        if n == n & -n:
            print('FastestFinger')
        else:
            print('Ashishgup')
    else:
        print('Ashishgup')


t = int(input())
for _ in range(t):
    solve()
