#   AtCoder abc056 a
#   ストレッチ課題

#   入力
a, b = list(map(str, input().split()))

#   判定
# if ((a == "H") and (b == "H")) or ((a == "D") and (b == "D")):
#     print("H")
# else:
#     print("D")
if a == b:
    print("H")
else:
    print("D")
