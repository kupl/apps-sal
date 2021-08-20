from math import gcd


def readinput():
    (n, x) = list(map(int, input().split()))
    xx = list(map(int, input().split()))
    return (n, x, xx)


def main(n, x, xx):
    y = [0] * len(xx)
    for i in range(len(xx)):
        y[i] = abs(xx[i] - x)
    if len(y) == 1:
        ans = y[0]
    else:
        ans = gcd(y[0], y[1])
        for i in range(2, n):
            ans = gcd(ans, y[i])
    return ans


def __starting_point():
    (n, x, xx) = readinput()
    ans = main(n, x, xx)
    print(ans)


__starting_point()
