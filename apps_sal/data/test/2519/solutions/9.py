N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

E = []

for i in range(N):
    E.append((P[i] + 1) / 2)

tnt = sum(E[:K])
ans = tnt

for i in range(N - K):
    tnt = tnt + E[K + i] - E[i]
    ans = max(ans, tnt)

print(ans)
