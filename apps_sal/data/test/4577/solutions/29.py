#   AtCoder abc061 a
#   ストレッチ課題

#   入力
a, b, c = list(map(int, input().split()))

#   判定
if (c >= a) and (c <= b):
    print("Yes")
else:
    print("No")
