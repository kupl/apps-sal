from copy import deepcopy
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    n, *a = map(int, read().split())

    if n == 2:
        r = [abs(a[1] * 2), abs(a[0] * 2)]
        print(*r, sep='\n')
        return

    amin = min(a)
    # 全aiを移動するコストを出す
    # 便宜のため、aの前後に0座標を追加する。
    a.insert(0, 0)
    a.append(0)
    # 単純化のため、aにマイナス座標がある(＝左の端がマイナス)なら、
    # 左の端＝座標0のコピーをつくる。マイナスではないなら単純コピー。
    if amin < 0:
        a2 = [i - amin for i in a]  # aminが正負どちらでもこれでOK
    else:
        a2 = deepcopy(a)
    # aを全て回った場合のコストを出す
    cost = 0
    for i1 in range(n + 1):
        cost += abs(a2[i1] - a2[i1 + 1])
    # rに答を格納する。aの前後に１要素足しているので長さを合わせる。
    r = [cost] * (n + 2)
    # a[i]それぞれをパスする場合のコストを出す。場合分けする。
    for j in range(1, n + 1):
        if a2[j - 1] <= a2[j] <= a2[j + 1]:
            continue
        elif a2[j - 1] >= a2[j] >= a2[j + 1]:
            continue
        elif a2[j - 1] <= a2[j] and a2[j + 1] <= a2[j]:
            nearer_dis = min(abs(a2[j - 1] - a2[j]), abs(a2[j] - a2[j + 1]))
            r[j] -= nearer_dis * 2
        else:
            nearer_dis = min(abs(a2[j] - a2[j - 1]), abs(a2[j + 1] - a2[j]))
            r[j] -= nearer_dis * 2
    print(*r[1:-1], sep='\n')


def __starting_point():
    main()


__starting_point()
