n = int(input())
tab = [int(i) for i in input().split()]
tab.sort()
dist = []
for i in range(n - 1):
    dist.append(tab[i + 1] - tab[i])
x = min(dist)
y = dist.count(x)
print(x, y)
