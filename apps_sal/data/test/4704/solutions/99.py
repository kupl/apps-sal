N = int(input())
A = list(map(int, input().split()))
S = sum(A)
snk = 0
arigm = S
ans = 1e+20
for i in range(N - 1):
    snk += A[i]
    arigm -= A[i]
    ans = min(abs(snk - arigm), ans)
print(ans)
