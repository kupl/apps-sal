N, M = map(int, input().split())
needs = []
for i in range(M):
    x, y = map(int, input().split())
    needs.append((x, y))
needs.sort(key=lambda x: x[1])
pb = needs[0][1]
res = 1
for i in needs:
    if i[0] >= pb:
        res += 1
        pb = i[1]

print(res)
