for _ in range(int(input())):

    n, x, m = map(int, input().split())
    l = x
    r = x
    for i in range(m):
        a, b = map(int, input().split())
        if a <= r and b >= l:
            r = max(b, r)
            l = min(a, l)
    print(r - l + 1)
