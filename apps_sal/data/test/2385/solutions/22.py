def main():
    from sys import stdin
    input = stdin.readline
    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0] * (n - 1)]

    g = [set() for _ in [0] * n]
    for a, b in ab:
        g[a - 1].add(b - 1)
        g[b - 1].add(a - 1)

    mod = 10**9 + 7
    fact = [1, 1]
    inv = [pow(i, mod - 2, mod) for i in range(n + 1)]
    for i in range(2, n + 1):
        fact.append(fact[-1] * i % mod)

    class rerooting():
        # addは頂点iに頂点jを根とする部分木（DPの値：x）をくっつけるときの補正
        def __init__(self, tree, ini):
            # merge:頂点aにbをマージするときのモノイド
            # adj_bu:ボトムアップ時の調整（a:値,i:頂点）
            # adj_td:トップダウン時の調整（a:値,i:頂点,p:親）
            # adj_fin:最終調整（a:値,i:頂点）
            def merge(a, b): return a * b % mod
            def adj_bu(a, i): return a * inv[size[i]] % mod
            def adj_td(a, i, p): return a * inv[n - size[i]] % mod
            def adj_fin(a, i): return a * fact[n - 1] % mod

            # トポロジカルソートをする
            # T:木の隣接グラフ表現をset化
            # P:親
            # q:キュー
            # order:トポソしたもの
            T = g
            P = [-1] * n
            q = [0]
            order = []
            while q:
                i = q.pop()
                order.append(i)
                for a in T[i]:
                    if a != P[i]:
                        P[a] = i
                        T[a].remove(i)
                        q.append(a)

            # Tをリストに変換
            T = [list(i) for i in T]

            # サイズの処理を先に行う
            # size[i]:0を根とする根付き木における、iを根とする部分木の大きさ
            size = [1] * n
            for i in order[1:][::-1]:
                size[P[i]] += size[i]

            # ボトムアップ処理をする
            # ME:マージした値を一時保存
            # DP:DP値、MEを調整したもの
            ME = [ini] * n
            DP = [0] * n
            for i in order[1:][::-1]:
                DP[i] = adj_bu(ME[i], i)
                p = P[i]
                ME[p] = merge(ME[p], DP[i])
            DP[order[0]] = adj_fin(ME[order[0]], order[0])
            TD = [ini] * n

            # トップダウン処理をする
            for i in order:
                # 左からDP（結果はTDに入れている）
                ac = TD[i]
                for j in T[i]:
                    TD[j] = ac
                    ac = merge(ac, DP[j])
                # 右からDP（結果はacに入れている、一度しか使わないのでacで問題ない）
                ac = ini
                for j in T[i][::-1]:
                    TD[j] = adj_td(merge(TD[j], ac), j, i)
                    ac = merge(ac, DP[j])
                    DP[j] = adj_fin(merge(ME[j], TD[j]), j)
            for i in DP:
                print(i)

    rerooting(g, 1)


main()
