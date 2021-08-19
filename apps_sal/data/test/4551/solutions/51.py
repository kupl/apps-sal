#   AtCoder abc083 a
#   ストレッチ課題

#   入力
a, b, c, d = list(map(int, input().split()))

#   判定
diff = (a + b) - (c + d)
if diff == 0:
    print("Balanced")
elif diff > 0:
    print("Left")
else:
    print("Right")
