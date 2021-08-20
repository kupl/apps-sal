n = int(input())
A = list(map(int, input().split()))
ans = R = X = 0
for L in range(n):
    while R < n and (not X & A[R]):
        X ^= A[R]
        R += 1
    ans += R - L
    X ^= A[L]
print(ans)
