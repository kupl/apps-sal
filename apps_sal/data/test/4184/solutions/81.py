# B - Balance

# 1～Nの番号がついたN個のおもりがあり、番号iの重さはWi
# 番号T以下の重りと番号Tより大きい重りの2グループに分け、それぞれのグループの重さの和をS1, S2とする
# この場合のS1とS2の差の絶対値の最小値を出力する

N = int(input())
W = list(map(int, input().split()))

S1 = 0
S2 = 0

answer = []

for i in range(N - 1):
    S1 += W[i]
    for j in range(i + 1, N):
        S2 += W[j]

    answer.append(abs(S2 - S1))
    S2 = 0

print(min(answer))
