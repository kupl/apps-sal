(n, v) = map(int, input().split())
l = []
for cont in range(0, n):
    l.append(list(map(int, input().split()))[1:])
ris = []
for cont in range(0, len(l)):
    for pr in l[cont]:
        if v > pr:
            ris.append(str(cont + 1))
            break
print(len(ris))
print(' '.join(ris))
