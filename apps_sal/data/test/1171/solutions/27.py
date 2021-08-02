# 初期入力
import bisect
import sys
input = sys.stdin.readline
N, K = (int(i) for i in input().split())
V = list(map(int, input().split()))
V_sorted = sorted(V)

# 取る個数take_num、返す個数reverse(t +r <=K)個全て決める

ans = []
take_V = []  # 最後に持っている宝石の価値
# Vが全てマイナスなら取らない
if V_sorted[-1] <= 0:
    ans = 0
else:
    take_num = min(K, N)
    for tak in range(1, take_num + 1):
        reverse = min(K - tak, tak)  # 返す数はtake_numではなく、Kから引く
        for lef in range(tak + 1):
            for rev in range(reverse + 1):

                take = []  # 取った宝石
                rig = N - (tak - lef)  # lef:左側の取る数 rig:右側の取る数
                take.extend(V[:lef])
                take.extend(V[rig:])
                take.sort()
                take_V.append(sum(take[rev:]))

    ans = max(take_V)
print(ans)
