def __starting_point():
    n, a, b = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    rev = arr[::-1]
    for i in range(n):
        if (arr[i] == 1 and rev[i] == 0) or (arr[i] == 0 and rev[i] == 1):
            print(-1)
            return
    ans = 0
    for i in range(n):
        if arr[i] == 2:
            if rev[i] == 0:
                ans += a
            elif rev[i] == 1:
                ans += b
            else:
                ans += min(a, b)
    print(ans)


__starting_point()
