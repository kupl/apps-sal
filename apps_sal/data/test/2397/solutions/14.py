def __starting_point():
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            b[i] = a[i]
        else:
            b[i] = b[i + 1] + a[i]
    ans = b[0]
    b[1:] = sorted(b[1:])
    k -= 1
    for i in range(n - 1, -1, -1):
        if k == 0:
            break
        ans += b[i]
        k -= 1
    print(ans)


__starting_point()
