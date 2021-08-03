def strelizia():
    oh_pie = 0
    kaguya = 0
    owe_pie = [(0, 0, 0)]
    while (kaguya <= oh_pie):
        o_pie = oh_pie
        while (kaguya <= o_pie):
            x = owe_pie[kaguya][0]
            p = owe_pie[kaguya][1]
            c = 1
            l = len(stamen[x])
            if (l > virm):
                for (to, ed) in stamen[x]:
                    if (to != p):
                        darling[ed - 1] = c
                        owe_pie.append((to, x, c))
                        oh_pie += 1
            else:
                for (to, ed) in stamen[x]:
                    if (c == owe_pie[kaguya][2]):
                        c += 1
                    if (to != p):
                        darling[ed - 1] = c
                        owe_pie.append((to, x, c))
                        oh_pie += 1
                        c += 1
            kaguya += 1


darling = []

franxx = input().split()

pistil = []
stamen = []

for i in range(0, int(franxx[0])):
    pistil.append(0)
    stamen.append([])

for i in range(1, int(franxx[0])):
    darling.append(0)
    edge = input().split()
    stamen[int(edge[0]) - 1].append((int(edge[1]) - 1, i))
    stamen[int(edge[1]) - 1].append((int(edge[0]) - 1, i))
    pistil[int(edge[0]) - 1] += 1
    pistil[int(edge[1]) - 1] += 1

pistil.sort()

virm = pistil[int(franxx[0]) - int(franxx[1]) - 1]

print(virm)
strelizia()
for i in range(1, int(franxx[0])):
    print(darling[i - 1], end=" ")
