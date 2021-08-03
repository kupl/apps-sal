N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = V[0]
for l in range(min(K, N) + 1):
    for r in range(min(K, N) - l + 1):
        v = V[:l] + V[N - r:]
        rest = K - (l + r)
        v.sort()
        tmp = 0
        for x in v:
            if rest and x < 0:
                rest -= 1
            else:
                tmp += x
        if ans < tmp:
            ans = tmp
print(ans)
