# 1つ目　縦A、横B
# 2つ目　縦C、横D
a, b, c, d = list(map(int, input().split()))
# 面積が大きい方を出力、等しい時は面積を出力

if a * b >= c * d:
    print((a * b))
else:
    print((c * d))
