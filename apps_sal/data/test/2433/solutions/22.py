n = int(input())
for i in range(n):
    b, c, d = list(map(int, input().split()))
    e, f = list(map(int, input().split()))
    ans = 0
    if f > e:
        ans += min(b // 2, d) * f
        b -= min(b // 2 * 2, d * 2)
        if b > 1:
            ans += min(b // 2, c) * e
    else:
        ans += min(b // 2, c) * e
        b -= min(b // 2 * 2, c * 2)
        if b > 1:
            ans += min(b // 2, d) * f
    print(ans)

