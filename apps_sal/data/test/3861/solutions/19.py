n = int(input())
a = list(map(int, input().split()))


def isSquare(a):
    if a < 0:
        return False
    (l, r) = (0, 1000001)
    while r - l > 1:
        mid = r + l >> 1
        if mid * mid > a:
            r = mid
        else:
            l = mid
    return l * l == a


print(max((x for x in a if not isSquare(x))))
