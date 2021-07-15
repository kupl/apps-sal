# 数値の取得
last,fee,cur = map(int,input().split())
feesqu = list(map(int,input().split()))
total = len(feesqu)

# コストの最小値を出力
tcost = 0
gcost = 0
for cnt in range(0,total,1):
    if feesqu[cnt] < cur:
        tcost += 1
gcost = total - tcost
print(min(tcost,gcost))
