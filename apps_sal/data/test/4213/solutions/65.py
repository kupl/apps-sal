# 長さNの整数列Aが与えられます。Aの（添字の）異なる2要素の差の絶対値の最大値を求めてください。

N = int(input())
A = list(map(int, input().split()))

print(max(A) - min(A))
