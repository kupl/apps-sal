from collections import deque

def main():
    with open(0) as f:
        N, *Temp = map(int, f.read().split())
        T, V = Temp[:N], Temp[N:]
        del Temp
    #v-tグラフを仮定して、各区間の境界条件を求める
    v_left = deque([0]) #初期時刻から走査した結果
    v_right = deque([0]) #終了時刻から走査した結果
    #区間i(1<=i<=N)の境界条件は [min(vin[i-1], vout[i-1]), max(vin[i], vout[i])
    #走査処理
    now = 0
    for t,v in zip(T, V):
        now = min(now+t, v)
        v_left.append(now)
    now = 0
    for t, v in zip(reversed(T), reversed(V)):
        now = min(now+t, v)
        v_right.appendleft(now)

    BC = [min(x,y) for x,y in zip(v_left, v_right)] #境界条件
    #区間ごとに2倍の面積計算
    S = [squareMeasure(vin, vout, vsup, t) for vin, vout, vsup, t in zip(BC[:N], BC[1:], V, T)]
    ans = sum(S)/2
    print(ans)

def squareMeasure(vin, vout, vsup, t):
    vmax = (t+vout+vin)/2 #y=x+vinとy=-x+t+vout の交点のy
    if vmax > vsup:
        a, b = vsup-vin, t+vout-vsup #y=vsupと2直線の交点
        S = (vin+vsup)*a + 2*(b-a)*vsup + (vsup+vout)*(t-b)
    else:
        S = (vin+vmax)*(vmax-vin) + (vmax+vout)*(t+vin-vmax)
    return S #2倍の面積である

def __starting_point():
    main()
__starting_point()
