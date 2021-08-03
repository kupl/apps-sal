N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

check = False

for i in range(N - M + 1):
    for j in range(N - M + 1):
        if A[i][j:j + M] == B[0]:
            flag = True
            for k in range(1, M):
                if A[i + k][j:j + M] != B[k]:
                    flag = False
            if flag:
                check = True

print("Yes" if check else "No")
