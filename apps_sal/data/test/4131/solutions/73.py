n, m = list(map(int, input().split()))
ps = [[] for _ in range(n)]

for i in range(m):
    p, y = list(map(int, input().split()))
    ps[p - 1].append((y, i))

for i in range(n):
    ps[i] = sorted(ps[i])

    pstr = str(i + 1).zfill(6)

    for j in range(len(ps[i])):
        ps[i][j] = (pstr + str(j + 1).zfill(6), ps[i][j][1])

ps = [city for sub in ps for city in sub]
ps = sorted(ps, key=lambda x: x[1])

for city in ps:
    print(city[0])
