def init(n):
    nonlocal par
    nonlocal size

    # 各頂点の親の番号(自身が根の場合は -1)
    # 最初は、どの頂点も根であるとして初期化
    par = [-1] * n

    # 各頂点の属するグループの頂点数(高さ)
    size = [1] * n


def unite(x, y):
    # [summary]xを含むグループと yを含むグループを併合する

    # 0インデックスに変更
    x -= 1
    y -= 1

    # x,yを それぞれ根まで移動する
    x = get_root(x)
    y = get_root(y)

    # すでに同じグループのときは 何もしない
    if x != y:
        # union by size(y側のサイズが小さくなるようにする)
        if size[x] < size[y]:
            x, y = y, x

        # yをxの子にする
        par[y] = x
        size[x] += size[y]


def get_root(x):
    # [summary]根を求める
    # その過程で、経路圧縮を行う(par[x]には、根が格納される)

    if par[x] == -1:
        # xが根の場合は、直接xを返す
        return x
    else:
        # xの親par[x]を根に張り替える
        # (ここで代入しておくことで、後の繰り返しを避けられる)
        # 各頂点の親子関係を知りたい場合は、この行をコメントアウト
        par[x] = get_root(par[x])

        return get_root(par[x])


def is_same(x, y):
    # [summary]xとyが同じグループに属するかどうか
    if get_root(x) == get_root(y):
        return True


def get_size(x):
    # [summary]xを含むグループの頂点数(高さ)

    return size[get_root(x)]


# B - Values
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

par = []
size = []

init(N)

for _ in range(M):
    c, d = map(int, input().split())

    # 各頂点の親子関係を記録
    unite(c, d)

groups = dict()

# 呼び出し元の処理
for i in range(N):
    r = get_root(i)

    if not r in groups.keys():
        groups[r] = [i]
    else:
        groups[r].append(i)

for vertexes in groups.values():
    a_sum = 0
    b_sum = 0

    for v in vertexes:
        a_sum += a[v]
        b_sum += b[v]

    if a_sum != b_sum:
        print('No')
        return

print('Yes')
