# 数値の取得
polynum = int(input())
length = list(map(int,input().split()))

# 図形の成立可否を検証し結果を出力
most_l = max(length)
othersum = sum(length) - most_l
if othersum > most_l:
    print("Yes")
else:
    print("No")
