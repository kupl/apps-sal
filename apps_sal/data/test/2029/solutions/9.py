koor = dict()
a = input()
q = int(a.split()[0])
w = int(a.split()[1])
for i in range(q - 1):
    a = input()
    z = int(a.split()[0])
    x = int(a.split()[1])
    if z not in list(koor.keys()):
        koor[z] = 1
    else:
        koor[z] += 1
    if x not in list(koor.keys()):
        koor[x] = 1
    else:
        koor[x] += 1
tt = list()
kolvo = 0
for i in list(koor.values()):
    if i == 1:
        kolvo += 1
print(w * 2 / kolvo)
