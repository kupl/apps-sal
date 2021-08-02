a, b, c, d, e, f = map(int, input().split())

water = [False] * (f // 100 + 1)
for i in range(0, len(water), a):
    water[i] = True
for i in range(len(water) - b):
    if water[i]:
        water[i + b] = True

sugar = [False] * ((f // 100) * e + 1)
for i in range(0, len(sugar), c):
    sugar[i] = True
for i in range(len(sugar) - d):
    if sugar[i]:
        sugar[i + d] = True

# denominator: 分母, numerator: 分子
deno = a * 100
nume = 0

for i in range(1, len(water)):
    if water[i]:
        j = min([i * e, f - 100 * i])
        while not sugar[j]:
            j -= 1
        i = 100 * i + j

        if nume * i < deno * j:
            deno = i
            nume = j

print(deno, nume)
