import math
n, m = list(map(int, input().split()))

modulo = [0 for x in range(0, m)]

for x in range(1, m + 1):
    modulo[(x * x) % m] += 1
# mnoze ile trzeba
for index in range(m):
    modulo[index] *= math.floor(n / m)

war = math.floor(n / m) * m
for x in range(war + 1, n + 1):
    modulo[(x * x) % m] += 1

suma = 0

for ind in range(1, m):
    war = modulo[ind] * modulo[m - ind]
    suma = suma + war


suma += modulo[0] * modulo[0]

print(suma)
