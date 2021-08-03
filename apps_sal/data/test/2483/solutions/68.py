N, C = map(int, input().split())

old = [[] for i in range(C)]

for i in range(N):
    s, t, c = map(int, input().split())
    old[c - 1].append((s, t))
ch = []
for li in old:
    li.sort()
    j = 0
    while(j < len(li)):
        start = li[j][0]
        while(j < len(li) - 1 and li[j][1] == li[j + 1][0]):
            j += 1
        end = li[j][1]
        ch.append((((start - 1) * 2) + 1, end * 2))
        j += 1


imos = [0] * (2 * 10**5 + 10)
for s, t in ch:
    imos[s] += 1
    imos[t] -= 1
for i in range(1, 2 * 10**5 + 10):
    imos[i] = imos[i - 1] + imos[i]
print(max(imos))
