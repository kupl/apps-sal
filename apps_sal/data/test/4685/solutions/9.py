(A, B, C) = map(int, input().split())
K = int(input())
M = sorted([A, B, C])
m = M[-1]
m = m * 2 ** K
print(m + M[0] + M[1])
