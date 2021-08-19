A, B, C, K = map(int, input().split())
# 1:A枚, 0:B枚, -1:C枚, K枚を選ぶ
A = min(A, K)
B = min(K - A, B)
C = min(K - A - B, C)
assert A + B + C >= K
#print(A, B, C)
print(A - C)
