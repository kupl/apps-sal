def main():
    n = int(input())
    a = list(map(int, input().split()))
    f, s = {}, {}
    for i in range(n):
        if i + 1 - a[i] not in list(f.keys()):
            f[i + 1 - a[i]] = 1
        else:
            f[i + 1 - a[i]] += 1
        if i + 1 + a[i] not in list(s.keys()):
            s[i + 1 + a[i]] = 1
        else:
            s[i + 1 + a[i]] += 1
    ans = 0
    for k in list(f.keys()):
        if k in list(s.keys()):
            ans += f[k] * s[k]
    print(ans)


def __starting_point():
    main()


__starting_point()
