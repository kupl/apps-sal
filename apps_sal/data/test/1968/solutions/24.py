n, v = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(list(map(int, input().split()))[1:])
ris = []
for cont in range(len(l)):
    for i in l[cont]:
        if v > i:
            ris.append(str(cont + 1))
            break
print(len(ris))
print(' '.join(ris))
