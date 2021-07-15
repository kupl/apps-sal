def main():
    h, w, n, *a = list(map(int, open(0).read().split()))
    l = [[i + 1] * a[i] for i in range(n)]
    s = sum(l, [])

    f = False
    ans = ''
    for i in range(h):
        x = s[i * w: (i + 1) * w]
        if f:
            x = x[::-1]
        f = not f
        ans += ' '.join(map(str, x)) + '\n'

    print(ans)


def __starting_point():
    main()

__starting_point()
