import sys
sys.setrecursionlimit(10**8)


def dfs(x, last=-1, ban_color=-1):
    """
    x: 今いる頂点
    last: 既に探索済の頂点(無限ループにならないように初期値-1)
    ban_color: 既に探索済の頂点(last)と今いる頂点(x)との辺に塗られている色(→使っちゃいけない色)
    """
    color = 1
    for to in vertex[x]:
        if to == last:
            continue
        if color == ban_color:
            color += 1
        color_dic[(x, to)] = color
        dfs(to, x, color)
        color += 1


n = int(input())
vertex = {i: [] for i in range(n)}
a = [0] * (n - 1)
b = [0] * (n - 1)
color_dic = {}


for i in range(n - 1):
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
