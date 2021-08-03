n = int(input())
s = list(map(int, input().split()))

pf = [[] for _ in range(10 ** 5 + 1)]
for i in range(2, 10 ** 5 + 1):
    if len(pf[i]) > 0:
        continue
    for j in range(i, 10 ** 5 + 1, i):
        pf[j].append(i)

f = [0] * (10 ** 5 + 1)

for x in s:
    for i in pf[x]:
        f[i] += 1

print(max(1, max(f)))
