(N, K) = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
m = 10 ** 9 + 7
a = [None] * (N + 1)
inva = [None] * (N + 1)
a[0] = 1
for i in range(1, N + 1):
    a[i] = i * a[i - 1] % m
inva[N] = pow(a[N], m - 2, m)
for i in range(N):
    inva[N - i - 1] = inva[N - i] * (N - i) % m
ans = 0
for i in range(N):
    if i < K - 1:
        continue
    tmp = a[i] * inva[i - K + 1] % m * inva[K - 1] % m
    ans += A[i] * tmp
    ans %= m
for i in range(N):
    if i > N - K:
        continue
    tmp = a[N - 1 - i] * inva[N - K - i] % m * inva[K - 1] % m
    ans -= A[i] * tmp
    ans %= m
print(ans)
