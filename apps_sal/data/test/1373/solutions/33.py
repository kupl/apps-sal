N, K = map(int, input().split())
M = 10**9 + 7
A = [0 for _ in range(N+1)]
RA = [0 for _ in range(N+1)]
for i in range(1, N+1):
    A[i] = A[i-1] + i

RA[0] = N
for j in range(1, N+1):
    RA[j] = N-j + RA[j-1]

ans = 0
# print(A)
# print(RA)
for k in range(K, N+2):
    minv = A[k-1]
    maxv = RA[k-1]
    ans += ((maxv - minv) + 1)%M
    ans %= M
    # print(k, (maxv-minv)+1)

print(ans)
