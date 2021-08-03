x = input()
z = input().split()

mx = 0
for i in z:
    pres = 0
    for a in i:
        if a >= 'A' and a <= 'Z':
            pres += 1
    if mx < pres:
        mx = pres
print(mx)
