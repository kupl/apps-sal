(N, K) = map(int, input().split())
V = list(map(int, input().split()))
result = 0
for a in range(N + 1):
    for b in range(N + 1):
        if a + b > K or a + b > N:
            break
        out = V[:a] + V[N - b:]
        out.sort()
        sum_val = sum(out)
        for i in range(min(a + b, K - a - b)):
            if out[i] >= 0:
                break
            sum_val -= out[i]
        result = max(result, sum_val)
print(result)
