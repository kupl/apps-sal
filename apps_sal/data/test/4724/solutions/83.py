#   AtCoder abc076 a
#   ストレッチ課題

#   入力
#   ミス　r, g = map(int, input().split())
r = int(input())
g = int(input())

#   処理
#   G = (R + answer) / 2 -> answer = 2G - R
answer = 2 * g - r

#   出力
print(answer)
