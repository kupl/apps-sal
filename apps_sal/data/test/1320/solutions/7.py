n = int(input())

r = 0
stlpce = [0 for i in range(n)]
for i in range(n):
    line = input()
    riadok = 0
    for j, c in enumerate(line):
        if c == 'C':
            riadok += 1
            stlpce[j] += 1
    r += riadok * (riadok - 1) // 2

for stlpec in stlpce:
    r += stlpec * (stlpec - 1) // 2

print(r)

