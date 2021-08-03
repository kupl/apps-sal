# 入力
N = int(input())
S = input()

target = 'ABC'
cnt = 0

# 1~3文字目、2~4文字目...のように１文字ずつスライドさせながら3つの連なる文字列を全探索する
for i in range(0, len(S) - 2):
    if S[i:i + 3] == target:
        cnt += 1

# カウントする
print(cnt)
