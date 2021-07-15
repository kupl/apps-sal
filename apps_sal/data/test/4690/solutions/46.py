A, B, C, D = map(int, input().split())

# 二つの長方形があります。
# 一つ目の長方形は、縦の辺の長さが A、横の辺の長さが Bです。
# 二つ目の長方形は、縦の辺の長さが C、横の辺の長さが Dです。
# この二つの長方形のうち、面積の大きい方の面積を出力してください。
# なお、二つの長方形の面積が等しい時は、その面積を出力してください。

area_ab = A * B
area_cd = C * D

if area_ab > area_cd:
    print(area_ab)
else:
    print(area_cd)
