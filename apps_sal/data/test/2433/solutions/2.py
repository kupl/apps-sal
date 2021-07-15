for cas in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    b //= 2
    ans = 0
    if h >= c:
        ans += min(b, p) * h
        b -= min(b, p)
        ans += min(b, f) * c
    else:
        ans += min(b, f) * c
        b -= min(b, f)
        ans += min(b, p) * h
    print(ans)
