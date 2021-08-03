n, m = map(int, input().split())
georg = list(map(int, input().split()))

good = list(map(int, input().split()))
good.sort()
georg.sort()
candoc = 0
j = 0
for i in range(min(n, m)):
    while j < m and good[j] < georg[i]:
        j += 1
    if j >= m:
        break
    if good[j] >= georg[i]:
        candoc += 1
        j += 1
    if j >= m:
        break
print(n - candoc)
