N = int(input())
A = int(input())

# N×Nのマス目があります
N *= N

# Aマスを白色に塗るとき、黒色に塗ることになるマスはいくつあるか出力
B = N - A
print(B)
