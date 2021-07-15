import numpy as np

n,k = map(int,input().split())
a = list(map(int,input().split()))
a = np.array(a)
a.sort()
plus = a[a>0]
zero = np.count_nonzero(a==0)
minus = a[a<0]

low = -10**20
hi = 10**20

while hi-low > 1:
    # n*nのマスからave以下という条件を満たす個数をカウントするイメージ
    item = 0
    ave = (hi+low)//2

    # aveがプラスの時ゼロの分は条件を満たすため加算してやる
    if ave >= 0:
        item += zero*n

    # bisect結果*(serchしたいplus) <= ave　を変形
    # bisect結果 <= ave//(serchしたいplus)　になる
    item += a.searchsorted(ave//plus,side='right').sum()

    # マイナスの方も式変形のやり方は同じ
    # マイナスの方は結果がaveより大きいものを除外する
    item += n*len(minus)-a.searchsorted(-(-ave//minus),side='left').sum()

    # 最後に条件は満たしているものの、自分自身をかけているものを引いてやる
    item -= np.count_nonzero(a*a <= ave)
    
    # 二分探索部分組み合わせの際に(a,b),(b,a)の２通り足してるので割る
    if item//2 >= k:
        hi = ave
    else:
        low = ave

print(hi)
