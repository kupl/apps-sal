for q11 in range(int(input())):
    (n, m) = list(map(int, input().split()))
    a = [int(q) - 1 for q in input().split()]
    s = [int(q) - 1 for q in input().split()]
    d = [0] * n
    for q in range(n):
        d[a[q]] = q
    (max1, ans) = (-1, 0)
    for q in range(m):
        if d[s[q]] > max1:
            ans += 2 * (d[s[q]] - q) + 1
            max1 = d[s[q]]
        else:
            ans += 1
    print(ans)
