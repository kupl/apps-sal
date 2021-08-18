from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
V = list(map(int, input().split()))
targ = min(N, K)

ans = -float("inf")

for i in range(targ + 1):
    for j in range(targ + 1 - i):
        get = sorted(V[:i] + V[N - j:])
        tmp = sum(get)
        for k in range(min(K - i - j, i + j)):
            tmp = max(tmp, tmp - get[k])

        ans = max(tmp, ans)

print(ans)
