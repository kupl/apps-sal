(h, w) = map(int, input().split())
ans = 10 ** 9
for (p, o) in zip([h, w], [w, h]):
    for i in range(1, p // 2 + 1):
        sa = i * o
        hi = (p - i) // 2
        sb = o * hi
        sc = o * (p - i - hi)
        t = max(sa, sb, sc) - min(sa, sb, sc)
        ans = min(ans, t)
        wi = o // 2
        sb = (p - i) * wi
        sc = (p - i) * (o - wi)
        t = max(sa, sb, sc) - min(sa, sb, sc)
        ans = min(ans, t)
print(ans)
