n, K = map(int, input().split())
arr = map(int, input().split())
freq = [0 for _ in range(K)]
for x in arr:
    freq[x % K] += 1
ans = 2 * (freq[0] // 2)
for i in range(1, K):
    if i < K - i:
        ans += 2 * (min(freq[i], freq[K - i]))
    elif i == K - i:
        ans += 2 * (freq[i] // 2)
print(ans)
