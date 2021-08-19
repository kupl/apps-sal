(n, size) = map(int, input().split())
pot = list()
tot = 0
for i in range(n):
    (a, b) = map(int, input().split())
    pot.append(a - b)
    tot += a
pot.sort()
pot = pot[::-1]
cpt = 0
while tot > size and cpt < len(pot):
    tot -= pot[cpt]
    cpt += 1
if tot > size:
    print(-1)
else:
    print(cpt)
