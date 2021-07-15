N, M = list(map(int, input().split()))
A = [input() for i in range(N)]
B = [input() for i in range(M)]

for i in range(N - M + 1):  # tate
    for j in range(N - M + 1):  # yoko
        ans = 1
        for k in range(M):
            if B[k] != A[i + k][j:j+M]:
                ans = 0
        if ans == 1:
            print('Yes')
            return
print('No')

