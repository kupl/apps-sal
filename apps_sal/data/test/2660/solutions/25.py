import heapq as hq
Q = int(input())
minval = 0
argminval = -(10**9)
#aを大きい方と小さい方に分けて最小ヒープで管理(Lは最大が欲しいので-1掛けておく)
L, R = [10**9], [10**9]
lenL, lenR = 0, 0

for _ in range(Q):
    qi = list(map(int, input().split()))
    if qi[0] == 1:
        ai, bi = qi[1], qi[2]
        LC, RC = -1*L[0], R[0] #左右それぞれで中央に一番近いもの
        if lenL == lenR:
            if ai < RC:
                #Lにaiを追加
                hq.heappush(L, -1*ai)
            else:
                #RCをLに移動, Rにaiを追加
                hq.heappop(R)
                hq.heappush(L, -1*RC)
                hq.heappush(R, ai)
            lenL += 1
            #新しいargminで最小値更新
            argminval = -1*L[0]
            minval += abs(argminval - ai) + bi
        else:
            if ai < LC:
                #LCをRに移動, Lにaiを追加
                hq.heappop(L)
                hq.heappush(L, -1*ai)
                hq.heappush(R, LC)
            else:
                #Rにaiを追加
                hq.heappush(R, ai)
            lenR += 1
            #古いargminで最小値更新
            minval += abs(argminval - ai) + bi
            argminval = -1*L[0]
    else:
        print("{} {}".format(argminval, minval))
