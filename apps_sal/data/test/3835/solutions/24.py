import math
N = int(input())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

M[0][0] = int(math.sqrt((M[0][1] * M[0][2]) / M[1][2]))

for n in range(1, N):
    M[n][n] = int(M[n - 1][n] / M[n - 1][n - 1])
ans = []
for n in range(N):
    ans.append(str(M[n][n]))
print(" ".join(ans))
