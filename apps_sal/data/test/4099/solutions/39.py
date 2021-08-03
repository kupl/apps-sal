# abc151B
# https://atcoder.jp/contests/abc151/tasks/abc151_b

# Ｎ科目テスト　各テストＫ点満点
# Ｎ-1科目のテストを受け、
# i番目の科目のテスト点数はＡi点
# Ｎ科目の平均点をＭ点以上にする
# 最後のテストで最低何点取る必要があるか

# 達成負不可の場合は"-1"を出力

# 入力
n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))

# 処理
# 最後のテストでの必要最低点を出力
a = sum(a)

score = (n * m) - a  # 最後の平均点の必要な値

if score <= k:
    answer = score if score > 0 else "0"
    print(answer)
else:
    print("-1")
