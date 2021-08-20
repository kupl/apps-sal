(N, M) = map(int, input().split())
A = [''] * N
B = [''] * M
for i in range(N):
    A[i] = input()
for i in range(M):
    B[i] = input()
match_cnt = 0
for i in range(N - M + 1):
    for j in range(N - M + 1):
        flag = True
        for y in range(M):
            if A[y + i][j:j + M] != B[y]:
                flag = False
        if flag:
            match_cnt += 1
if match_cnt > 0:
    print('Yes')
else:
    print('No')
