from sys import stdin
entrada = 0

sumatotal = 0


for line in stdin:
    linea1 = line.splitlines()
    break


a = int(linea1[0].split()[0])
b = int(linea1[0].split()[1])

arreglo = []

for x in input().split():
    arreglo.append(int(x))


arreglo.sort()
sumatotal = sum(arreglo[:b])


print(sumatotal)
