(N, M) = list(map(int, input().split()))
A = []
B = []
C = []
D = []
for i in range(N):
    (x, y) = list(map(int, input().split()))
    A.append(x)
    B.append(y)
for i in range(M):
    (x, y) = list(map(int, input().split()))
    C.append(x)
    D.append(y)
for i in range(N):
    ans = []
    for j in range(M):
        tmp = abs(A[i] - C[j]) + abs(B[i] - D[j])
        ans.append(tmp)
    T = len(ans)
    for k in range(T):
        if ans[k] == min(ans):
            print(k + 1)
            break
