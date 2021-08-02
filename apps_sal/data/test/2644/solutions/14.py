N = int(input())
*P, = map(int, input().split())

Q = [0] * (N + 1)
for i, p in enumerate(P, 1):
    Q[p] = i

ans = []
i = 1
while(i < N):
    j = Q[i]
    if j <= i: break
    for k in range(j - 1, i - 1, -1):
        ans.append(k)
        P[k], P[k - 1] = P[k - 1], P[k]
    i = j

if len(ans) == N - 1:
    if P == list(range(1, N + 1)):
        for out in ans:
            print(out)
    else:
        print(-1)
else:
    print(-1)
