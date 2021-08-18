n, m, p = list(map(int, input().split()))
s = [int(i) for i in input().split()]

p_size = [0] * p
field = []
field_free = 0
pp = [set() for _ in range(p)]
for y in range(n):
    for x, i in enumerate(input()):
        if not (i == '.' or i == '#'):
            pp[int(i) - 1].add(x + y * m)
        c = i != '#'
        field_free += int(c)
        field.append(c)


def append_nearest(fp, ppn, pi):
    nonlocal field_free
    nonlocal p_size
    if not field[fp]:
        return
    if fp % m > 0 and field[fp - 1]:
        ppn.add(fp - 1)
    if fp % m < m - 1 and field[fp + 1]:
        ppn.add(fp + 1)
    if fp // m > 0 and field[fp - m]:
        ppn.add(fp - m)
    if fp // m < n - 1 and field[fp + m]:
        ppn.add(fp + m)
    field[fp] = False
    field_free -= 1
    p_size[pi] += 1


for pi in range(p):
    ppi = pp[pi]
    ppn = pp[pi] = set()
    for fp in ppi:
        append_nearest(fp, ppn, pi)
    del ppi

ppn = set()
for pi in range(p):
    ppi = pp[pi]
    if len(ppi) > 0:
        for _ in range(s[pi]):
            for fp in ppi:
                append_nearest(fp, ppn, pi)
            ppi.clear()
            ppi, ppn = ppn, ppi

            if field_free == 0 or len(ppi) == 0:
                break
        pp[pi] = ppi

        if field_free == 0:
            break
nmlp = n * m - m
ssss = True
while field_free > 0 and ssss:
    ssss = False
    for pi in range(p):
        ppi = pp[pi]
        if len(ppi) > 0:
            for _ in range(s[pi]):
                for fp in ppi:
                    if not field[fp]:
                        continue
                    if fp % m > 0 and field[fp - 1]:
                        ppn.add(fp - 1)
                    if fp % m < m - 1 and field[fp + 1]:
                        ppn.add(fp + 1)
                    if fp > m - 1 and field[fp - m]:
                        ppn.add(fp - m)
                    if fp < nmlp and field[fp + m]:
                        ppn.add(fp + m)
                    field[fp] = False
                    field_free -= 1
                    p_size[pi] += 1
                ppi.clear()
                ppi, ppn = ppn, ppi
            pp[pi] = ppi
            ssss |= len(ppi) > 0


print(' '.join(map(str, p_size)))
