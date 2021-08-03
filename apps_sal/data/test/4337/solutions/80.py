# 数値と文字の取得
num = int(input())
colors = list(map(str, input().split()))

# 黄色があるか判定し結果を出力
if colors.count("Y") > 0:
    print("Four")
else:
    print("Three")
