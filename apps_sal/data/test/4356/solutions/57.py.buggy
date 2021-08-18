N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
for i in range(N - M + 1):
    for j in range(N - M + 1):
        flg = True
        for k in range(M):
            for l in range(M):
                flg = flg & (B[k][l] == A[i + k][j + l])

        if flg:
            ans = 'Yes'
            print(ans)
            return

ans = 'No'
print(ans)
