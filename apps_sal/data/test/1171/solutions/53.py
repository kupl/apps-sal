(N, K) = list(map(int, input().split()))
V = list(map(int, input().split()))
ans = 0
for gets in range(min(N, K) + 1):
    for lgets in range(gets + 1):
        rgets = gets - lgets
        haves = V[:lgets] + V[N - rgets:]
        haves.sort()
        removes = K - gets
        for i in range(min(removes, len(haves))):
            if haves[i] < 0:
                haves[i] = 0
            else:
                break
        ans = max(ans, sum(haves))
print(ans)
