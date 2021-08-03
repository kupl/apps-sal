# 直角三角形ABCがあります。∠ABC=90°です。三角形ABCの三辺の長さである|AB|,|BC|,|CA|が与えられるので、直角三角形ABCの面積を求めて下さい。
# ただし、三角形ABCの面積は整数となることが保証されています。

AB, BC, CA = map(int, input().split())
print((AB * BC) // 2)
