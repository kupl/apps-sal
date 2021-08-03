N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0

for a in range(min(N, K) + 1):
    for b in range(min(N, K) - a + 1):
        cur = V[:a] + V[N - b:]
        cur.sort()

        idx = 0
        while idx < min(K - a - b, len(cur)):
            if cur[idx] > 0:
                break
            else:
                idx += 1

        ans = max(ans, sum(cur[idx:]))

print(ans)
