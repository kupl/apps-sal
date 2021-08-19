(N, M) = map(int, input().split())
ks = [list(map(int, input().split())) for i in range(M)]
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** N):
    s = i
    b = [0] * N
    for j in range(N):
        if s >= 2 ** (N - j - 1):
            s -= 2 ** (N - j - 1)
            b[j] = 1
    for j in range(M):
        on = 0
        for k in range(ks[j][0]):
            if b[ks[j][k + 1] - 1] == 1:
                on += 1
        if on % 2 != p[j]:
            break
    else:
        ans += 1
print(ans)
