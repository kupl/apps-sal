#   AtCoder abc058 a
#   ストレッチ課題

#   入力
a, b, c = list(map(int, input().split()))

#   判定
if (b - a) == (c - b):
    print("YES")
else:
    print("NO")
