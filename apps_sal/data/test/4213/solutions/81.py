N = int(input())
A = list(map(int, input().split()))

# Aの（添字の）異なる2要素の差の絶対値の最大値を出力せよ。

print(max(A) - min(A))
