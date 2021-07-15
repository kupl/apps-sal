#   AtCoder abc075 a
#   ストレッチ課題

#   入力
a, b, c =list(map(int, input().split()))

#   判定
if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)

