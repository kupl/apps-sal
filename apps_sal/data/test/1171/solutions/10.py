from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
V = list(map(int, input().split()))
targ = min(N, K)

ans = -float("inf")

#i: 左から取る回数
for i in range(targ + 1):
    #j: 右を取る回数
    for j in range(targ + 1 - i):
        get = sorted(V[:i] + V[N - j:])
        tmp = sum(get)
        for k in range(min(K - i - j, i + j)):
            tmp = max(tmp, tmp - get[k])

        ans = max(tmp, ans)

print(ans)
