def gcd(a, b):
    """最大公約数"""
    if b == 0:
        return a
    return gcd(b, a % b)


def mapt(fn, *args):
    return list(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    N, X = Input()
    x = Input()

    if N == 1:
        print(abs(x[0] - X))
        return

    x.append(X)
    x.sort()
    data = [abs(x[i] - x[i + 1]) for i in range(N)]

    ans = data[0]
    for i in range(1, N):
        ans = gcd(data[i], ans)
    print(ans)


main()
