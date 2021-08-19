n = int(input())
l = list(map(int, input().split(' ')))
l.sort()
nb = 0
for i in range(n):
    if l[i] == -1:
        continue
    h = 1
    nb += 1
    for j in range(i + 1, n):
        if l[j] >= h:
            h += 1
            l[j] = -1
print(nb)
