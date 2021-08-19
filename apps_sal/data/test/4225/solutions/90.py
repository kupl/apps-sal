(A, B, C, K) = map(int, input().split())
A = min(A, K)
B = min(K - A, B)
C = min(K - A - B, C)
assert A + B + C >= K
print(A - C)
