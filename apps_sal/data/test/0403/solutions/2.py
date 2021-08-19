[n, x, y] = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
c = 0
for i in a:
    chislo = i
    if chislo // 2 <= x:
        ax = i // 2
    else:
        ax = x
    x -= ax
    chislo = chislo - ax * 2
    ay = min(chislo, y)
    y -= ay
    chislo = chislo - ay
    if chislo != 0 and x != 0:
        x -= 1
        chislo -= 1
    if chislo == 0:
        c += 1
    else:
        break
print(c)
