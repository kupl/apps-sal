# 入力を受け取る
N = int(input())
S = input()

# 切り出した3文字がabcだったらcouontを1upする
count = 0

for i in range(len(S) - 3 + 1):
    if S[i] + S[i + 1] + S[i + 2] == 'ABC':
        count += 1

# countを出力する
print(count)
