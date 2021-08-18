
ais = list(map(int, input().strip().split()))


def do(i):
    ris = list(ais)
    r = ris[i]
    ris[i] = 0
    for j in range(14):
        ris[(i + 1 + j) % 14] += (r // 14) + int((r % 14) > j)
    return sum(ri for ri in ris if (ri % 2 == 0))


m = 0
for i in range(14):
    if ais[i] > 0:
        m = max(m, do(i))

print(m)
