
# 1行目の入力は使用しない
input()
# 2行目の入力は整数の配列として取得
A = list(map(int, input().split()))

# 最大のAiを設定
max_A = 0
# output
sum_A = 0

for Ai in A:
    max_A = max(Ai, max_A)
    if max_A > Ai:
        sum_A += max_A - Ai

print(sum_A)
