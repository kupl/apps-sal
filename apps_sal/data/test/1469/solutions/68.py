# 頂点は0番から始まるとして、出力時に+1する
def graph(L):
    beki = 1
    for n in range(20):
        beki *= 2
        if beki > L: break

    ans = []
    Li = 1
    for i in range(n):
        ans += [(i + 1, i + 2, 0)]
        ans += [(i + 1, i + 2, Li)]
        Li *= 2

    Lnext = Li
    nokori_kosu = L - Li
    i = n - 1
    way_i = Li // 2
    while nokori_kosu > 0:
        while way_i > nokori_kosu:
            way_i //= 2
            i -= 1
        ans += [(i + 1, n + 1, Lnext)]
        Lnext += way_i
        nokori_kosu -= way_i
    print((n + 1, len(ans)))
    for x in ans:
        print((*x))


L = int(input())
graph(L)

