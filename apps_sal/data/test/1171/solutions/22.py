N, K = list(map(int, input().split()))
V = list(map(int, input().split()))
r = min(N, K)
ans = 0
for a in range(r + 1):
    for b in range(r - a + 1):
        tmp, minus = 0, []
        for i in range(a):
            t = V[i]
            tmp += t
            if t < 0:
                minus.append(t)
        for j in range(b):
            t = V[N - 1 - j]
            tmp += t
            if t < 0:
                minus.append(t)
        tmp -= sum(sorted(minus)[:K - (a + b)])
        ans = max(ans, tmp)
print(ans)
