(N, M) = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort(key=lambda x: x[0])
(x, y) = [list(i) for i in zip(*xy)]
nokori = M
ans = 0
for i in range(N):
    ans += x[i] * min(y[i], nokori)
    nokori -= y[i]
    if nokori <= 0:
        break
print(ans)
