X = int(input())

# 現在の貯金額100円（年間利子1％）
# 預金額が初めて X円以上 になるのは何年後かを出力

count = 0
saving = 100

while saving < X:
    saving += saving // 100
    count += 1

print(count)
