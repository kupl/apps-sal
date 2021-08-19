def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = input()
    (ans, s) = (0, 0)
    for i in range(n):
        if k[i] == '1':
            ans = max(ans + a[i], s)
        s += a[i]
    print(ans)


def __starting_point():
    main()


__starting_point()
