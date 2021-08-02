N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))
B = sorted(A)
C = [0] * (N + 1)
cnt_1 = 0
cnt_2 = 0

for i in range(M):
    C[B[i]] += 1

for j in range(1, N - X):
    cnt_1 += C[X + j]

for k in range(1, X + 1):
    cnt_2 += C[X - k]

cnt = [cnt_1, cnt_2]

print((min(cnt)))
