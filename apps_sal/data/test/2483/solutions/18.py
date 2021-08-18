imos = [0] * (10**5 + 2)

N, C = map(int, input().split())
C = 30
mitai = [[] for i in range(C + 1)]

for i in range(N):
    s, t, c = map(int, input().split())
    mitai[c].append([s, t])

for i in range(C + 1):
    mitai[i].sort()


for i in range(C + 1):
    preT = -1
    for j in mitai[i]:
        s, t = j[0], j[1]
        if preT == s:
            imos[s + 1] += 1
            imos[t + 1] -= 1
        else:
            imos[s] += 1
            imos[t + 1] -= 1
        preT = t

for i in range(1, len(imos)):
    imos[i] = imos[i - 1] + imos[i]

print(max(imos))
