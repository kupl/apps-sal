#   AtCoder abc063 a
#   ストレッチ課題

#   入力
a, b = list(map(int, input().split()))

#   処理
if (a + b) >= 10:
    print("error")
else:
    print((a + b))
