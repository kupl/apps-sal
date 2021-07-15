# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())
A = list(map(int,input().split()))

# B[i] : i桁目が 1 になっているAの要素数
B = [0] * 40
for a in A:
    for i in range(40):
        if a&(1<<i):
            B[i] += 1

# K以下の条件を無視した場合の, 最適な X
# これは桁ごとに最適値を調べれば良い
X = [0]*40
for i in range(40):
    if B[i] <= N/2:
        X[i] = 1

# K を X に合わせた表現にする
bitK = list(map(int, list(bin(K)[2:].zfill(40)[::-1])))

# 初期値はKと一致した場合にしておく
ans = 0
for i in range(40):
    if bitK[i]==1:
        ans += (N-B[i])<<i
    else:
        ans += B[i]<<i

# Kと不一致になる最上位の桁
for k in range(40):
    # 0の桁で不一致になることはあり得ない
    if bitK[k]==0:
        continue

    total = 0
    leqK = False 
    for i in range(39,-1,-1):
        # K以下が確定しているなら, 貪欲に最適値をとる
        if leqK:
            if X[i]==1:
                total += (N-B[i])<<i
            else:
                total += B[i]<<i
        # そうでないなら
        else:
            # Kと不一致になる最上位の桁 であるなら, X の該当桁を 0 として不一致にする
            if i==k:
                total += B[i]<<i
                leqK = True
            # Kと一致している
            else:
                if bitK[i]==1:
                    total += (N-B[i])<<i
                else:
                    total += B[i]<<i
    ans = max(total,ans)

print(ans)
