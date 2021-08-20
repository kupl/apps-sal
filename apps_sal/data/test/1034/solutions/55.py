(X, Y, Z, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
ans = []
for i in range(min(X, K)):
    D = int(K / (i + 1)) + 1
    for j in range(min(D, Y, K)):
        E = int(D / (j + 1)) + 1
        for k in range(min(E, Z, K)):
            ans.append(A[i] + B[j] + C[k])
ans.sort(reverse=True)
for i in range(K):
    print(ans[i])
