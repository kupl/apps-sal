a = input().split()
a = [int(i) for i in a]
b = input().split()
b = [int(i) for i in b]
c = input().split()
c = [int(i) for i in c]
cha = []
for i in range(0, a[1] - 1):
    cha.append(b[i] - b[a[1] - 1])
cao = []
for i in range(1, a[1]):
    cao.append(c[0] - c[-i])
dui = 0
cha.sort()
cao.sort()
i = 0
j = 0
while j < a[1] - 1:
    if cha[i] <= cao[j]:
        dui += 1
        i += 1
        j += 1
    else:
        j += 1
print(a[1] - dui)
