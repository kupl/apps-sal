def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = [0] * n
    c[n - 1] = 1
    s = [False] * 100001
    s[a[n - 1]] = True
    for i in range(1, n):
        if s[a[n - i - 1]]:
            c[n - i - 1] = c[n - i]
        else:
            c[n - i - 1] = c[n - i] + 1
            s[a[n - i - 1]] = True
    print('\n'.join(str(c[int(input()) - 1]) for _ in range(m)))


def __starting_point():
    main()


__starting_point()
