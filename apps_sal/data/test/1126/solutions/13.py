N, X, M = map(int, input().split())
ans = 0
A = []
sa = set(A)
while N:
    if X not in sa:
        ans += X
        A.append(X)
        sa.add(X)
        X = X**2 % M
        N -= 1
    else:
        i = A.index(X)
        B = A[i:]
        L = len(B)
        ans += sum(B) * (N // L) + sum(B[:N % L])
        N = 0
print(ans)
