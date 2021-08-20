MOD = 1000000007
(N, M) = list(map(int, input().split()))
cnt = [0 for _ in range(N + 1)]
cnt[0] = 1
for _ in range(M):
    a = int(input())
    cnt[a] = -1
for i in range(1, N + 1):
    if cnt[i] == -1:
        cnt[i] = 0
        continue
    if i == 1:
        cnt[i] = cnt[i - 1]
    else:
        cnt[i] = (cnt[i - 1] + cnt[i - 2]) % MOD
print(cnt[N])
