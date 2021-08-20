(N, K) = list(map(int, input().split()))
V = list(map(int, input().split()))
ans = 0
for l in range(K + 1):
    for r in range(K - l + 1):
        if l + r > N:
            continue
        d = K - l - r
        now = 0
        having = []
        for i in range(l):
            now += V[i]
            having.append(V[i])
        for i in range(N - r, N):
            now += V[i]
            having.append(V[i])
        having.sort()
        for i in range(d):
            if i >= len(having):
                break
            if having[i] >= 0:
                break
            now -= having[i]
        ans = max(ans, now)
print(ans)
