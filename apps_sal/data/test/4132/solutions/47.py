from math import gcd


def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    return (n, a)


def main(n, a):
    ans = gcd(a[0], a[1])
    for i in range(2, n):
        ans = gcd(ans, a[i])
    return ans


def __starting_point():
    (n, a) = readinput()
    ans = main(n, a)
    print(ans)


__starting_point()
