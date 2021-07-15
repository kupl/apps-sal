def d_no_need(N, K, A):
    card = sorted(A, reverse=True)
    s = 0  # カードの値の総和
    ans = 0  # 不必要なカードの枚数
    # Aのうち要素が大きいものから見ていったとき、
    # その要素を入れても総和がK未満のものだけ加えていく
    # 最後に連続して加えた要素の個数が解となる
    # (それら以外の要素の組み合わせでK以上にでき、かつ、
    #  それらの総和がK未満になるため)
    for a in card:
        if s + a < K:
            s += a
            ans += 1
        else:
            ans = 0
    return ans

N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print(d_no_need(N, K, A))
