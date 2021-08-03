N, M = (input().split())
N = int(N)
M = int(M)

L = [0] * M
R = [0] * M

for i in range(M):
    L_i, R_i = (input().split())
    L[i] = int(L_i)
    R[i] = int(R_i)

print(max(min(R) - max(L) + 1, 0))
