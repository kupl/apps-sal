N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = [0]
b = [0]

for i in range(N):
    a.append(a[i] + A[i])
for j in range(M):
    b.append(b[j] + B[j])
ans = 0
j = M
for i in range(N + 1):
    if a[i] > K:
        break
    while a[i] + b[j] > K:
        j -= 1
    ans = max(ans, i + j)
print(ans)
