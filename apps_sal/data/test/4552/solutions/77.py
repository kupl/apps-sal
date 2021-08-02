N = int(input())
F = [list(map(int, input().split())) for n in range(N)]
P = [list(map(int, input().split())) for n in range(N)]
ans = []

for i in range(1, 1024):
    p = 0
    for j in range(N):
        c = 0
        for k in range(10):
            if (i >> k & 1) & F[j][k]:
                c += 1
        p += P[j][c]
    ans += [p]

print(max(ans))
