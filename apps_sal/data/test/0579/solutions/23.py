from numba import jit


@jit
def main():
    n, k = list(map(int, input().split(" ")))
    p = list(map(int, input().split(" ")))
    c = list(map(int, input().split(" ")))
    ans = -10**18
    for i in range(n):
        start, count = i, 1
        val = c[start]
        while p[start] - 1 != i:  # ループ部分. iに戻る直前まで続ける.
            start = p[start] - 1
            count += 1
            val += c[start]
        start = i
        # この時点でvalは1ループのスコア合計, カウントは1ループのsizeになっている
        '''
    以下の基本的な方針は
    - 1ループ分のスコア合計が正であればできるだけループしてスコアを稼ぎ、残りの余りの分の最大をとる。
    - 1ループ分のスコア合計が負であればループ回数を0にして、1ループ以内で最大となる移動を求める。
    しかし、ループ回数が最大であればいいとは限らない。
    x回ループできたとしてcount%k回の余りの分を調べても、x-1回ループし次の1回のループのなかで1周仕切らない移動が最大になる可能性がある。
    なのでx-1回分のループだけ取り切ってしまい、残りcount+k%count(＝「1周半」)の中で最大を調べる必要がある。
    また、負の場合は基本的に1周以内だが、kが極端に小さいときの処理が必要。
    '''
        if val > 0:
            a = (k // count - 1) * val  # 最後に余りのk%count回ぶんだけでなく1周半ぶんは試したいので(ループ余りではk%count回しか移動できないわけではない)
            ans = max(a, ans)
            num = count + k % count
        else:
            a = 0
            num = min(k, count)  # 1周以内におさめたい. k<countという非常に限られた場合のみk回までの移動になることを考慮。
        for _ in range(num):
            start = p[start] - 1
            a += c[start]
            ans = max(a, ans)
    print(ans)


main()
