(N, K) = list(map(int, input().split()))
l = [0] * K
for i in range(1, N + 1):
    l[i % K] += 1
ans = 0
for ai in range(K):
    bi = (K - ai) % K
    ci = (K - ai) % K
    if (bi + ci) % K == 0:
        ans += l[ai] * l[bi] * l[ci]
print(ans)
