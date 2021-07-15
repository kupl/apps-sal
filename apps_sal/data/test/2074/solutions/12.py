n, m = (int(i) for i in input().split())
masha = {}
pasha = {}
max = 0
vybor = 0
for i in range(1, n+1):
    street = [int(i) for i in input().split()]
    mininstreet = min(street)
    pasha.update({i:mininstreet})
    if max <= mininstreet:
        max = mininstreet
        vybor = i
print(pasha[vybor])
