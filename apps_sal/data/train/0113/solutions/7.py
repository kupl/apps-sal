t = int(input())
while t:
    t -= 1
    (a, b) = map(int, input().split())
    if a > b:
        (a, b) = (b, a)
    d = b - a
    ans = 0
    if d >= 5:
        ans += d // 5
        d %= 5
    if d >= 2:
        ans += d // 2
        d %= 2
    if d >= 1:
        ans += d
    print(ans)
