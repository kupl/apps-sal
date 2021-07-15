import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

# 左の箱（パターンにあたる）と右の箱（対象）が連動して動く
# 文字が同じ限り右に広げて、lcpを記録しながら左に縮めていく感じ
# 縮められなくなったら、topを右の箱の左端にして、左の箱を0までずらす
# 箱ができていない（幅が0）のときは、右の箱を1つ右に

def ZAlgorithm(aa):
    target = aa
    # s = input()
    len_t = len(target)
    lcp = [-1] * len_t
    top = 1  # 右の箱において、左の箱の0に対応する点
    left = 0  # 左の箱の左端(本当はここでので宣言は不要だけど理解の為)
    right = 0  # 左の箱の右端
    lcp[0] = 0
    while top < len_t:
        # 箱を右に広げていく
        while top + right < len_t and target[right] == target[top + right]:
            right += 1
        # 右の箱左端のlcpを記録
        lcp[top] = right
        left = 1
        # 箱の幅が0だったらtopを動かして、このターン終了
        if right == 0:
            top += 1
            continue
        # lcpを記録しながら箱を左に縮めていく（最初の条件重要）
        while left + lcp[left] < right and left < right:
            lcp[top + left] = lcp[left]
            left += 1
        # topを右の箱の左端にして、左の箱を0まで戻す
        top += left
        right -= left
        left = 0  # これも本当は不要
    return lcp

def main():
    # 「aを左にシフト」＝「bを右にシフト」
    # 左にシフトは面倒なのでbを右に動かす
    # 動かした(下記は2つシフトしたとき)結果
    #  a0  a1  a2  a3  a4
    # xor xor xor xor xor
    #  x   x   x   x   x
    #  =   =   =   =   =
    #  b3  b4  b0  b1  b2
    # と、なっていればよい。ここで、xorをただの足し算に置き換えて考える
    #  a0  a1  a2  a3  a4
    #  +   +   +   +   +
    #  x   x   x   x   x
    #  =   =   =   =   =
    #  b3  b4  b0  b1  b2
    # 具体例で
    #  4   6   3   7   2
    #  +   +   +   +   +
    #  1   1   1   1   1
    #  =   =   =   =   =
    #  5   7   4   8   3
    # このとき、aの増減とbの増減は一致する
    # aの増減・・・末尾から(+2) 4 (+2) 6 (-3) 3 (+4) 7 (-5) 2
    # bの増減・・・末尾から(+2) 5 (+2) 7 (-3) 4 (+4) 8 (-5) 3
    # これはxorでも同様のことがいえる
    # よって、a,bそれぞれの隣接xorのリストを作る
    # aを2つ並べて(ループするから)、bを右にシフトしながら一致する位置を探す
    # 一致する位置を探すのはZ-Algorithmを使った
    # シフト量が分かれば、対応する1組のa,bからxも分かる
    # らしいが、こんなの思いつかんわ!!

    inf = pow(2, 31)
    n = II()
    aa = LI()
    bb = LI()
    ax = [aa[i - 1] ^ aa[i] for i in range(n)]
    bx = [bb[i - 1] ^ bb[i] for i in range(n)]
    # print(ax)
    # print(bx)
    ll = ZAlgorithm(bx + [inf] + ax + ax[:-1])
    # lcp・・・length common prefixみたいな?
    for shift, lcp in enumerate(ll[n + 1:]):
        if lcp == n: print(shift, aa[shift] ^ bb[0])

main()

