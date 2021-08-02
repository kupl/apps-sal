def main():
    n, k = list(map(int, input().split()))
    s = input()
    L = []
    if s[0] == '0':
        z = 1
        l = 0
    else:
        z = 0
    for i in range(n):
        if s[i] == '0' and z == 0:
            l = i
            z = 1
        elif s[i] == '1' and z == 1:
            L.append([l, i - 1])
            z = 0
    if z == 1:
        L.append([l, n - 1])
    ans = 0
    if len(L) <= k:
        ans = n
    else:
        l = 0
        r = L[k][0] - 1
        if r - l + 1 > ans:
            ans = r - l + 1
        for i in range(1, len(L) - k):
            l = L[i - 1][1] + 1
            r = L[i + k][0] - 1
            if r - l + 1 > ans:
                ans = r - l + 1
        l = L[-k - 1][1] + 1
        r = n - 1
        if r - l + 1 > ans:
            ans = r - l + 1
    print(ans)


def __starting_point():
    main()


__starting_point()
