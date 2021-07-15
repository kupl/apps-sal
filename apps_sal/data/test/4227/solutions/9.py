import itertools

n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a][b] = 1
    g[b][a] = 1

a = list(itertools.permutations(range(n)))
ans = 0
for i in a:
    if i[0] != 0:
        break
    for j in range(n-1):
        if g[i[j]][i[j+1]] == 0:
            break
    else:
        ans += 1
print(ans)
