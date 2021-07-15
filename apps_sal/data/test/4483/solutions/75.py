# 入力
X = int(input())
A = int(input())
B = int(input())

# A円のケーキを1個買う
balance = X - A

# 残金で買えるケーキBの数を求める
quantity = balance // B

# Bのケーキを変えるだけ買う
balance -= B * quantity

# 残金を出力する
print(balance)
