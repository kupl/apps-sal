(N, M) = map(int, input().split())
A = []
for i in range(N):
    a = list(input())
    A.append(a)
B = []
for i in range(M):
    b = list(input())
    B.append(b)
ans = 'No'
for i in range(N - M + 1):
    for j in range(N - M + 1):
        if A[i][j] == B[0][0]:
            count = 0
            for k in range(M):
                for l in range(M):
                    if A[i + k][j + l] == B[k][l]:
                        count += 1
            if count == M * M:
                ans = 'Yes'
                break
print(ans)
