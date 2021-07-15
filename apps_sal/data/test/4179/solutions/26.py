def main():
    n, m, c = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = []

    cnt = 0
    for i in range(n):
        a.append(list(map(int, input().split())))

    for i in range(n):
        ans = 0
        for k in range(m):
            ans += a[i][k] * b[k]
        if ans + c > 0:
            cnt += 1
    print(cnt)


def __starting_point():
    main()

__starting_point()
