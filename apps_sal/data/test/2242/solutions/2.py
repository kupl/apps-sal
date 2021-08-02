S = input()
N = len(S)
A = [int(S[i]) for i in range(N)]
A = A[::-1]

MOD = 2019

p10 = [1] * N
for i in range(1, N):
    p10[i] = (p10[i - 1] * 10) % MOD

for i in range(N):
    A[i] = (A[i] * p10[i]) % MOD

cumsum = [A[0]] * N
for i in range(1, N):
    cumsum[i] = (cumsum[i - 1] + A[i]) % MOD

cnt = [0] * MOD
cnt[0] = 1
for i in range(N):
    cnt[cumsum[i]] += 1

ans = 0
for i in range(MOD):
    ans += cnt[i] * (cnt[i] - 1) // 2

print(ans)
