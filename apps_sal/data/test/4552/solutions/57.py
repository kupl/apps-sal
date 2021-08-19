N = int(input())
(F, P) = ([], [])
for i in range(N):
    F.append(list(map(int, input().split())))
for i in range(N):
    P.append(list(map(int, input().split())))
ans = -10 ** 9
for i in range(1, 2 ** 10):
    l = [0] * N
    for j in range(10):
        if i >> j & 1:
            for k in range(N):
                if F[k][j] == 1:
                    l[k] += 1
    tmp = 0
    for m in range(N):
        n = l[m]
        tmp += P[m][n]
    ans = max(tmp, ans)
print(ans)
