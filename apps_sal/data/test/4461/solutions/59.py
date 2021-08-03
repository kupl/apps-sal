def abc062_c():
    h, w = map(int, input().split())
    # 2 <= h, w のため1の場合は考えない
    # どちらかが3の倍数ならぴったり3分割できる (平行2線)
    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return
    # 平行2線で割るときの差分最小は、短辺1本分
    ans = min(h, w)
    # それ以外は例2例3の割り方 (直交2線)
    for x, y in [(w, h), (h, w)]:
        for i in range(1, x):
            sa = i * y
            sb = (x - i) * (y // 2)
            sc = (x - i) * (y - y // 2)
            diff = max(sa, sb, sc) - min(sa, sb, sc)
            ans = min(diff, ans)
    print(ans)


abc062_c()
