N, K = map(int, input().split())
ans = 0
for i in range(N):
    prob = 1 / N
    temp = i + 1
    while temp < K:
        temp *= 2
        prob *= 0.5
    ans += prob

print(ans)
