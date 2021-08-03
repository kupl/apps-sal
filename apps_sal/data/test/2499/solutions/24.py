import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def main():
    n = int(input())
    aa = list(map(int, input().split()))
    s = 0
    # s=総xorを求める
    for a in aa:
        s ^= a
    # print(format(s, "b"))

    # sで1がたっている桁はaの選び方で影響を受けないので、aのその桁を0にする
    for i in range(n):
        # print(format(aa[i], "b"), end=" ")
        aa[i] &= ~s
        # print(format(aa[i], "b"))

    # 掃き出し法
    rnk = 0  # ランク
    for k in range(60, -1, -1):
        # k桁目に1がたっているaを探す(kは0-indexed)
        mask = 1 << k
        for i in range(rnk, n):
            if mask & aa[i]:
                aa[i], aa[rnk] = aa[rnk], aa[i]
                break
        else:
            continue
        # 見つかったa以外のk桁目をすべて0にするため、k桁目が1のaに、見つかったaをxorする
        for i in range(n):
            if i == rnk:
                continue
            if aa[i] & mask:
                aa[i] ^= aa[rnk]
        rnk += 1

    # できるだけ上位に1が来るよう、aを選んでいく
    red = 0
    for i in range(rnk):
        red ^= aa[i]
    blue = s ^ red
    # red+blue=(red xor blue)+2*(red & blue)
    print((s + 2 * (red & blue)))


main()
