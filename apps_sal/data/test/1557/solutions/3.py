h1, a1, c1 = list(map(int, input().split()))
h2, a2 = list(map(int, input().split()))
an = []
while h2 > 0:
    if h2 - a1 <= 0:
        an.append('STRIKE')
        break
    if h1 <= a2:
        h1 += c1
        an.append('HEAL')
    else:
        h2 -= a1
        an.append('STRIKE')
    h1 -= a2
print(len(an))
for i in an:
    print(i)
