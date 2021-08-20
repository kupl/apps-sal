(n, h, m) = list(map(int, input().split()))
maksi = [h] * n
tab = [[] for i in range(m)]
for i in range(m):
    tab[i] = list(map(int, input().split()))
for i in range(m):
    l = tab[i][0]
    r = tab[i][1]
    for j in range(l - 1, r):
        maksi[j] = min(maksi[j], tab[i][2])
wyn = 0
for i in range(n):
    wyn += maksi[i] ** 2
print(wyn)
