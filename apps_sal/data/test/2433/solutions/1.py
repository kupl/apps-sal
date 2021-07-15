for _ in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    if h < c:
        h, c = c, h
        p, f = f, p
    ham = min(p, b // 2)
    ans = ham * h
    b -= 2 * ham
    chicken = min(f, b // 2)
    ans += chicken * c
    print(ans)
