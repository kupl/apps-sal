def d_patisserie_abc():
    N, M = [int(i) for i in input().split()]
    Cake = [[int(i) for i in input().split()] for j in range(N)]
    # 変数の意味は，左から順に， 綺麗さ, おいしさ, 人気度 をそれぞれ
    # 正の方向 (p) に最大化する場合と負の方向 (n) に最大化する場合である．
    # なお，nnn, nnp, npn, npp は，ppp, ppn, pnp, pnn を
    # 逆にすることで得られる．
    ppp, ppn, pnp, pnn = [], [], [], []
    for x, y, z in Cake:
        ppp.append(x + y + z)
        ppn.append(x + y - z)
        pnp.append(x - y + z)
        pnn.append(x - y - z)
    ppp.sort()
    ppn.sort()
    pnp.sort()
    pnn.sort()

    # 値が大きなものを M 個取って足して絶対値をとる
    pts = map(lambda x: abs(sum(x)),
              (ppp[:M], ppn[:M], pnp[:M], pnn[:M], ppp[::-1][:M],
               ppn[::-1][:M], pnp[::-1][:M], pnn[::-1][:M])
              )
    return max(pts)

print(d_patisserie_abc())
