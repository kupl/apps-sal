def main():
    (n, m) = list(map(int, input().split()))
    ans = []
    t = [True] * (n + 1)
    l = n // 2 - 1
    for i in range(1, n // 2):
        if l <= 0:
            break
        if not t[i] or not t[i + l]:
            continue
        ans.append([i, i + l])
        t[i] = False
        t[i + l] = False
        l -= 2
    if n % 2 == 1:
        l = n // 2
        for i in range(n // 2, n):
            if l <= 0:
                break
            if not t[i] or not t[i + l]:
                continue
            ans.append([i, i + l])
            t[i] = False
            t[i + l] = False
            l -= 2
    else:
        l = n // 2 - 2
        for i in range(n // 2, n):
            if l <= 0:
                break
            if not t[i] or not t[i + l]:
                continue
            ans.append([i, i + l])
            t[i] = False
            t[i + l] = False
            l -= 2
    for i in range(m):
        print((ans[i][0], ans[i][1]))


def __starting_point():
    main()


__starting_point()
