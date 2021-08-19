def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def solve(x, y, a, b):
    ans = ''
    while not x == 1 or not y == 1:
        if x < y:
            (x, y, a, b) = (y, x, b, a)
        ans += str((x - 1) // y) + a
        x = x - (x - 1) // y * y
    print(ans)


(x, y) = list(map(int, input().split()))
if gcd(x, y) > 1:
    print('Impossible')
else:
    solve(x, y, 'A', 'B')
