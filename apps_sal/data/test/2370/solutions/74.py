def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = m[i][j]
            for k in range(n):
                if k in (i, j):
                    continue
                t = m[i][k] + m[k][j]
                if t < d:
                    print((-1))
                    return
                if t == d:
                    break
            else:
                ans += d
    else:
        print(ans)


def __starting_point():
    main()

__starting_point()
