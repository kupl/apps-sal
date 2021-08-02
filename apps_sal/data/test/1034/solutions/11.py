X, Y, Z, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

ans = []
for i in range(X):
    for j in range(Y):
        ij = (i + 1) * (j + 1)
        if ij > K:
            break
        for k in range(Z):
            if ij * (k + 1) > K:
                break
            ans.append(A[i] + B[j] + C[k])
ans = sorted(ans, reverse=True)
for i in range(K):
    print(ans[i])
