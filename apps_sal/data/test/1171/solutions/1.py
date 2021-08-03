N, K, *V = list(map(int, open(0).read().split()))

# i: 操作回数
# j: 取り出す個数
# k: 左から取り出す範囲 [0, k)
ans = 0
for i in range(K + 1):
    for j in range(min(N + 1, i + 1)):
        for k in range(j + 1):
            right = N - j + k
            tmp = V[:k] + V[right:]
            tmp.sort()
            ans = max(ans, sum(tmp) - sum([t for t in tmp if t < 0][: i - j]))
print(ans)
