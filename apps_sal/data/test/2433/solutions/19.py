t = int(input())
while t:
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    ans = 0
    if h > c:
        ans += min(b // 2, p) * h
        b -= 2 * p
        if b > 0:
            ans += min(b // 2, f) * c
    else:
        ans += min(b // 2, f) * c
        b -= 2 * f
        if b > 0:
            ans += min(b // 2, p) * h
    print(ans)
    t -= 1
