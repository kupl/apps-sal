import itertools
N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -10**9
for i in list(itertools.product(range(2), repeat=10)):
    if sum(i) == 0:
        continue
    bns = 0
    for j in range(N):
        b = 0
        for k in range(10):
            if i[k] * F[j][k] == 1:
                b += 1
        bns += P[j][b]
    ans = max(ans, bns)
print(ans)
