ricetta = input()
(nb, ns, nc) = [int(x) for x in input().split()]
(pb, ps, pc) = [int(x) for x in input().split()]
(b, s, c) = (0, 0, 0)
r = int(input())
for x in ricetta:
    if x == 'B':
        b += 1
    if x == 'S':
        s += 1
    if x == 'C':
        c += 1
x = 0
y = 2
prezzo = 0
while x < y:
    prezzo = max(0, pb * b * y - nb * pb) + max(0, pc * c * y - nc * pc) + max(0, ps * s * y - ns * ps)
    if prezzo < r:
        x = y
        y = 2 * y
    if prezzo > r:
        y = (x + y) // 2
    if prezzo == r:
        x = y
print(x)
