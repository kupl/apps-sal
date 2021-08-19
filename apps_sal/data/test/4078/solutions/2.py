(n, m) = list(map(int, input().split()))
mas = list(map(int, input().split()))
otmas = []
for i in range(m):
    otmas.append(list(map(int, input().split())))
for i in range(m):
    otmas[i][0] -= 1
    otmas[i][1] -= 1
ans = -1
masotv = []
for i in range(n):
    mascop = mas.copy()
    masotvizc = []
    for j in range(m):
        if not (i >= otmas[j][0] and i <= otmas[j][1]):
            masotvizc.append(j + 1)
            for k in range(otmas[j][0], otmas[j][1] + 1):
                mascop[k] -= 1
    if max(mascop) - min(mascop) > ans:
        masotv = masotvizc
    ans = max(ans, max(mascop) - min(mascop))
print(ans)
print(len(masotv))
print(*masotv)
