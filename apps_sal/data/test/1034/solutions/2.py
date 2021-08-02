x, y, z, K = list(map(int, input().split()))
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)
ans = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            if (i + 1) * (j + 1) * (k + 1) <= K:
                ans.append(A[i] + B[j] + C[k])
                continue
            break
ans.sort(reverse=True)

for i in range(K):
    print((ans[i]))
