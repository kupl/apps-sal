l = []
for i in range(5):
    l.append(int(input()))
amari = []
for i in range(5):
    if 10 - l[i] % 10 == 10:
        amari.append(0)
    else:
        amari.append(10 - l[i] % 10)
jikan = []
for i in range(5):
    if amari[i] == 10:
        jikan.append(l[i])
    else:
        jikan.append(l[i] + amari[i])

print((sum(jikan) - max(amari)))
