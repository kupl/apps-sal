N = int(input())
S = list(range(1, N + 1))
H = [sorted(list(map(int, input().split()))) for i in range(N - 1)]
F = 0
tyouten = int(N * (N + 1) * (N + 2) / 6)
for i in range(len(H)):
    F += H[i][0] * (N - H[i][1] + 1)
print(tyouten - F)
