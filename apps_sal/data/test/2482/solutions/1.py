N, K, L = map(int, input().split())


def fp(x, parentList):  # findParent
    if parentList[x] == x:
        return x
    else:
        parentList[x] = fp(parentList[x], parentList)
        return parentList[x]


# 各ノードのparentをリストで表現(連結前は自身がparent)
road = [i for i in range(N)]
rail = [i for i in range(N)]

for _ in range(K):
    p, q = map(int, input().split())
    par_p, par_q = fp(p - 1, road), fp(q - 1, road)  # p, qのparent
    # 連結する際、若い番号をparentとする
    if par_p < par_q:
        road[par_q] = par_p
    else:
        road[par_p] = par_q

# railについても同様
for _ in range(L):
    s, t = map(int, input().split())
    par_s, par_t = fp(s - 1, rail), fp(t - 1, rail)
    if par_s < par_t:
        rail[par_t] = par_s
    else:
        rail[par_s] = par_t

# 連結成分の要素をカウント
cnt = {}
for i in range(N):
    key = (fp(i, road), fp(i, rail))
    if key in cnt:
        cnt[key] += 1
    else:
        cnt[key] = 1
# 出力
for i in range(N):
    key = (fp(i, road), fp(i, rail))
    ans = cnt[key]
    print(ans, end=" ")
