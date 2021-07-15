# 数値の取得
N = int(input())
Hlist = list(map(int, input().split()))

# 最小値の取得と出力
Vcnt = 0
for cnt in range(0,N,1):
    maxH = max(Hlist[:cnt+1])
    if Hlist[cnt] >= maxH:
        Vcnt += 1

print(Vcnt)
