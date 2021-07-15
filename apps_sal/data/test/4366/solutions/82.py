#   AtCoder abc057 a
#   ストレッチ課題

#   入力
a, b = list(map(int, input().split()))

#   処理
if (a + b) >= 24:
    answer = (a + b) - 24
else:
    answer = a + b
print(answer)

