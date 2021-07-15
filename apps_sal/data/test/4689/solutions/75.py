def __starting_point():

    k,n = list(map(int,input().split()))
    A = list(map(int,input().split()))

    #距離の差分が一番多い区間を求める
    sbn = -1
    for i in range(n-1):
        sbn = max(sbn,A[i+1]-A[i])

    #最初と最後も比較する
    tmp1 = A[0] - 0
    tmp2 = k - A[n-1]
    sbn = max(sbn,tmp1+tmp2)

    print((k-sbn))


__starting_point()
