n, p = [int(x) for x in input().split()]
mi = []
for k in range(0, n):
    l, r = [int(x) for x in input().split()]
    x = (r // p - (l - 1) // p) / (r - l + 1)
    mi.append(1 - x)

fin = 0
for z in range(0, len(mi)):
    fin += (1 - mi[z] * mi[(z + 1) % n])
print(fin * 2000)
