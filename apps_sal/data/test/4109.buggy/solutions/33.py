(N, M, X) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]
d = []
for i in range(2 ** N):
    b = [0] * (M + 1)
    e = i
    for j in range(N):
        if e >= 2 ** (N - j - 1):
            e -= 2 ** (N - j - 1)
            for k in range(M + 1):
                b[k] += a[j][k]
    c = 1
    for j in range(1, M + 1):
        if b[j] < X:
            c = 0
            break
    if c == 1:
        d.append(b[0])
if len(d) > 0:
    ans = min(d)
else:
    ans = -1
print(ans)
