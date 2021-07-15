import itertools

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

c = list(itertools.combinations(range(n), 2))
ans = 0
for a, b in c:
    dist = 0
    for j in range(d):
        dist += (x[a][j]-x[b][j])**2
    if dist**(1/2) % 1 == 0:
        ans += 1
print(ans)
