n = int(input())
a = list(map(int, input().split()))
lang = dict()
cnt = [0] * n
count = 0
for l in a:
    if l not in lang:
        lang[l] = count
        count += 1
    cnt[lang[l]] += 1
m = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
bestfilm = 0
bestsat = 0 if b[0] not in lang else cnt[lang[b[0]]]
bestpartsat = 0 if c[0] not in lang else cnt[lang[c[0]]]
for i in range(m):
    sat = 0 if b[i] not in lang else cnt[lang[b[i]]]
    partsat = 0 if c[i] not in lang else cnt[lang[c[i]]]
    if sat > bestsat or (sat == bestsat and bestpartsat < partsat):
        bestfilm = i
        bestsat = sat
        bestpartsat = partsat
print(bestfilm + 1)
