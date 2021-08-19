(N, K) = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for l in range(N + 1):
    for r in range(N + 1):
        if l + r > N or l + r > K:
            break
        arr = V[:l]
        if r:
            arr += V[-r:]
        arr.sort()
        rem = K - l - r
        tmp = 0
        for a in arr:
            if a < 0 and rem:
                rem -= 1
            else:
                tmp += a
        ans = max(ans, tmp)
print(ans)
