(n, m) = map(int, input().split())
voyage = [set() for i in range(n + 1)]
for i in range(m):
    (a, b) = map(int, input().split())
    voyage[a].add(b)
    voyage[b].add(a)
ans = 0
for v in voyage[1]:
    if v in voyage[n]:
        ans = 1
print('POSSIBLE' if ans else 'IMPOSSIBLE')
