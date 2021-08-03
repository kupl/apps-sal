t = int(input())
for query in range(t):
    b, p, f = list(map(int, input().split()))
    h, c = list(map(int, input().split()))
    if h > c:
        ans = h * min(b // 2, p)
        b -= min(b // 2, p) * 2
        ans += c * min(b // 2, f)
        print(ans)
    else:
        ans = c * min(b // 2, f)
        b -= min(b // 2, f) * 2
        ans += h * min(b // 2, p)
        print(ans)
