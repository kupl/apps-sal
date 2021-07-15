#   AtCoder abc067 a
#   ストレッチ課題

#   入力
a, b = list(map(int, input().split()))

#   判定
if (a % 3 == 0) or (b % 3 == 0) or ((a + b) % 3 == 0):
    print("Possible")
else:
    print("Impossible")

