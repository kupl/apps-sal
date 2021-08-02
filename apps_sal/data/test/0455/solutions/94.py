def solve(x, y, d, m):
    ret = ""
    for i in range(m):
        if x + y >= 0 and x - y >= 0:
            ret += "R"
            x -= d[i]
        elif x + y >= 0 and x - y < 0:
            ret += "U"
            y -= d[i];
        elif x + y < 0 and x - y >= 0:
            ret += "D"
            y += d[i];
        else:
            ret += "L"
            x += d[i]
    print(ret)


def main():
    m = 34
    X, Y, d = [], [], []

    for i in range(32, 0, -1):
        d += [2**i]
    d += [1]

    N = int(input())
    even, odd = 0, 0

    for i in range(N):
        x, y = list(map(int, input().split()))
        X += [x]; Y += [y]

        if (abs(x) + abs(y)) % 2 == 0:
            even += 1
        else:
            odd += 1

    if even and odd:
        print((-1))
        return 0

    if odd:
        m -= 1
    else:
        d += [1]

    print(m)
    print((" ".join(map(str, d))))

    for i in range(N):
        solve(X[i], Y[i], d, m)


main()
