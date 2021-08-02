from functools import reduce
n = int(input())
L = list(map(int, input().split()))


def gcd(x, y):
    if y > x:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


ans = reduce(gcd, L)
print(ans)
