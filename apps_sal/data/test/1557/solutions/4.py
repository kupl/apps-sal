(h1, a1, c1) = map(int, input().split())
(h2, a2) = map(int, input().split())
coms = []
while h2 > 0:
    if h2 <= a1:
        coms.append('STRIKE')
        h2 -= a1
    elif h1 <= a2:
        coms.append('HEAL')
        h1 += c1
    else:
        coms.append('STRIKE')
        h2 -= a1
    h1 -= a2
print(len(coms))
print(*coms, sep='\n')
