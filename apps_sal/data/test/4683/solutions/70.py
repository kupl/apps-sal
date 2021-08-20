N = int(input())
A = [0] * N
S = [0] * (N + 1)
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
for i in range(N):
    S[i + 1] = (S[i] + A[i]) % mod
cnt = 0
for j in range(N - 1):
    cnt += A[j] * (S[N] - S[j + 1]) % mod
print(cnt % mod)
