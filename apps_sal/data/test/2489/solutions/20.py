N = int(input())
A = [int(_) for _ in input().split()]
A.sort()
M = max(A)
X = [True for _ in range(M + 1)]
for a in set(A):
    if not X[a]:
        continue
    for v in range(2 * a, M + 1, a):
        X[v] = False
for i in range(N - 1):
    if A[i] == A[i + 1]:
        X[A[i]] = False
ans = 0
for a in A:
    if X[a]:
        ans += 1
print(ans)
