#   AtCoder abc064 a
#   ストレッチ課題

#   入力
r, g, b = list(map(int, input().split()))

#   処理
answer = r * 100 + g *10 + b

#   判定
if (answer % 4) == 0:
    print("YES")
else:
    print("NO")

