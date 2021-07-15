N = int(input())
F = [0] * N
for i in range(N):
    F[i] = list(map(int, input().split()))

P = [0] * N
for i in range(N):
    P[i] = list(map(int, input().split()))

ans = -float("inf")

for j in range(1, 1024):
    ss = 0
    for i in range(N):
        b = format(j, "010b")
        bb = [0] * 10
        for k in range(10):
            bb[k] = F[i][k] * int(b[k])
        ss += P[i][sum(bb)]
    ans = max(ans, ss)

print(ans)
