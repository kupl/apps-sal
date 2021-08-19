import sys
sys.setrecursionlimit(10**8)


def dfs(x, last=-1, ban_color=-1):
    """
    x: 今いる頂点
    last: 既に探索済の頂点(無限ループにならないように初期値-1)
    ban_color: 既に探索済の頂点(last)と今いる頂点(x)との辺に塗られている色(→使っちゃいけない色)
    """
    color = 1
    for to in vertex[x]:  # 今いる頂点に隣接する頂点(つまり今いる頂点から出てる辺をすべて舐める),(rootから隣接する頂点に対してのroopとも捉えられる)
        if to == last:
            continue  # 既に探索済の辺はもう色が塗られているからスキップ
        if color == ban_color:
            color += 1
        color_dic[(x, to)] = color  # 辺の色をぬる
        dfs(to, x, color)
        color += 1


n = int(input())
vertex = {i: [] for i in range(n)}  # 隣接頂点を保持
a = [0] * (n - 1)  # i番目の辺を保持
b = [0] * (n - 1)  # i番目の辺を保持
color_dic = {}  # 辺の色を保持


for i in range(n - 1):  # 隣接頂点の辞書を作成
    a[i], b[i] = list(map(int, input().split()))
    a[i] -= 1
    b[i] -= 1
    vertex[a[i]].append(b[i])
    vertex[b[i]].append(a[i])

max_v = 0

for _, v in list(vertex.items()):
    if len(v) > max_v:
        max_v = len(v)
print(max_v)


dfs(0)

for i in range(n - 1):
    if (a[i], b[i]) in color_dic:
        print((color_dic[(a[i], b[i])]))
    else:
        print((color_dic[(b[i], a[i])]))
