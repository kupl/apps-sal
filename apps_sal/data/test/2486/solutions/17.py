def d_NoNeed(N, K, A):
    a = sorted(A)
    s = t = 0
    # aのうち要素が大きいものから見ていったとき、
    # その要素を入れても総和がK未満のものだけ加えていく
    # 最後に連続して加えた要素の個数が解となる
    # (それら以外の要素の組み合わせでK以上にでき、かつ、
    #  それらの総和がK未満になるため)
    for i in range(N - 1, -1, -1):
        if s + a[i] < K:
            s += a[i]
            t += 1
        else:
            t = 0
    return t

N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print(d_NoNeed(N, K, A))
