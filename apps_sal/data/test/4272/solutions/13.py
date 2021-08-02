# 文字数Nを取得
N = int(input())

# 文字列Sを取得
S = input()

target = 'ABC'
counter = 0

# 1文字目〜3文字目、2文字目〜4文字目、...というように3文字ずつ比較してスライドするを繰り返すことで全探索する
for i in range(0, len(S) - 2):
    if S[i:i + 3] == target:
        counter += 1

# カウントを出力
print(counter)
