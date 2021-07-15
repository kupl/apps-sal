for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    cur = b
    if cur < a:
        if d >= c:
            print(-1)
            continue
        delta = c - d
        cur += c * ((a - cur + delta - 1) // delta)
    print(cur)
