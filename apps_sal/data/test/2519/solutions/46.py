(N, K) = map(int, input().split())
p = list(map(lambda x: int(x) + 1, input().split()))
ans = sum(p[0:K])
s = ans
for i in range(1, N - K + 1):
    s += p[i + K - 1] - p[i - 1]
    ans = max(ans, s)
print(ans / 2)
