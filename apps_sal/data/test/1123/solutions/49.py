(N, K) = list(map(int, input().split()))
mod = int(1000000000.0 + 7)
A = [0] * (K + 1)
ans = 0
for i in range(K, 0, -1):
    A[i] = pow(K // i, N, mod)
    idx = 2 * i
    while idx <= K:
        A[i] = (A[i] - A[idx]) % mod
        idx += i
    ans = (ans + A[i] * i) % mod
print(ans)
