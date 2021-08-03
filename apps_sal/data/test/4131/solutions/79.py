n, m = list(map(int, input().split()))
city = [list(map(int, input().split())) for _ in range(m)]
pref = [[] for _ in range(n + 1)]

ans = []

for i, c in enumerate(city):
    pref[c[0]].append([i, c[1]])

for i in range(n):
    pref[i + 1].sort(key=lambda x: x[1])
    for j in range(len(pref[i + 1])):
        ans.append([pref[i + 1][j][0], str(i + 1).zfill(6) + str(j + 1).zfill(6)])

ans.sort(key=lambda x: x[0])

for c in ans:
    print((c[1]))
