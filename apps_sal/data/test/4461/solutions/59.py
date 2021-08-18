def abc062_c():
    h, w = map(int, input().split())
    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return
    ans = min(h, w)
    for x, y in [(w, h), (h, w)]:
        for i in range(1, x):
            sa = i * y
            sb = (x - i) * (y // 2)
            sc = (x - i) * (y - y // 2)
            diff = max(sa, sb, sc) - min(sa, sb, sc)
            ans = min(diff, ans)
    print(ans)


abc062_c()
