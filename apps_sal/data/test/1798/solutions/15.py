a = int(input())
seq = list(map(int, input().split()))
mass = {}
for i in range(a):
    if seq[i] in mass:
        mass[seq[i]].append(i)
    else:
        mass[seq[i]] = [i]
tmp_mass = []
for key, value in list(mass.items()):
    flag = True
    if len(value) == 1:
        tmp_mass.append((key, 0))
        continue
    elif len(value) == 2:
        tmp_mass.append((key, value[1] - value[0]))
        continue
    else:
        for i in range(len(value) - 2):
            if value[i + 2] - value[i + 1] == value[i + 1] - value[i]:
                pass
            else:
                flag = False
        if flag:
            tmp_mass.append((key, value[len(value) - 1] - value[len(value) - 2]))
print(len(tmp_mass))
tmp_mass.sort(key=lambda x: x[0])
for i in range(len(tmp_mass)):
    print(' '.join(map(str, tmp_mass[i])))
