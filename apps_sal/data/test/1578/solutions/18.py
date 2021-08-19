# サンプル2を適当にsum(range)したらなんかわかった
# 愚直にrangeするとTLEなるので等差数列の和を使う
n = int(input())
x = (n * (n + 1)) // 2
print((x - n))
