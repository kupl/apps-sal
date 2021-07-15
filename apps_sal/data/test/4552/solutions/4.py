N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -10**10

for a in range(2**10):
    t = [(a>>b)&1 for b in range(10)]
    if 1 not in t:
        continue
    
    p = 0
    for i in range(N):
        p += P[i][sum(t[j] and F[i][j] for j in range(10))]

    ans = max(p, ans)

print(ans)
