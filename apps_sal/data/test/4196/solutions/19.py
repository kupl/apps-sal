def main():

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    n = int(input())
    a = [int(x) for x in input().split()]
    x = [0] * n
    y = [0] * n
    for i in range(1, n):
        x[i] = gcd(x[i - 1], a[i - 1])
    for i in range(n - 2, -1, -1):
        y[i] = gcd(y[i + 1], a[i + 1])
    ans = [gcd(x[i], y[i]) for i in range(n)]
    print(max(ans))


def __starting_point():
    main()


__starting_point()
