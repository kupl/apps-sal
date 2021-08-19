(H, W) = map(int, input().split())
(L, side, ver) = ([], [], [])
for i in range(H):
    a = list(input())
    L.append(a)


def check(n, inlist, outlist):
    """[summary]
    全て白マスの行を削除する
    転置行列を返すので列の判定にも対応可能
    Args:
        n ([type]): 配列サイズ
        inlist ([type]): 入力する二次元配列
        outlist ([type]): 出力する二次元配列

    Returns:
        [list]: 不要な要素を削除して転置して返す
    """
    for i in range(n):
        if ('#' in inlist[i]) == True:
            outlist.append(inlist[i])
    return list(map(list, zip(*outlist)))


side = check(H, L, side)
ver = check(len(side), side, ver)
for i in range(len(ver)):
    print(''.join(ver[i]))
