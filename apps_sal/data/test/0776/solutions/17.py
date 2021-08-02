(u, p, b) = tuple(map(int, input().split()))
n = int(input())
equiped = 0
fullPrice = 0
arrusb = []
arrpc2 = []
for k in range(n):
    (price, mtype) = tuple(input().split())
    if mtype == "USB":
        arrusb.append(int(price))
    else:
        arrpc2.append(int(price))

arrusb.sort()
arrpc2.sort()
bcounter = 0
pcounter = 0

for i in range(n):
    if bcounter == len(arrusb):
        if p > 0:
            fullPrice += arrpc2[pcounter]
            p -= 1
            equiped += 1
        elif b > 0:
            fullPrice += arrpc2[pcounter]
            b -= 1
            equiped += 1
        pcounter += 1
        continue

    if pcounter == len(arrpc2):
        if u > 0:
            fullPrice += arrusb[bcounter]
            u -= 1
            equiped += 1
        elif b > 0:
            fullPrice += arrusb[bcounter]
            b -= 1
            equiped += 1
        bcounter += 1
        continue

    if arrusb[bcounter] < arrpc2[pcounter]:
        if u > 0:
            fullPrice += arrusb[bcounter]
            u -= 1
            equiped += 1
        elif b > 0:
            fullPrice += arrusb[bcounter]
            b -= 1
            equiped += 1
        bcounter += 1
    else:
        if p > 0:
            fullPrice += arrpc2[pcounter]
            p -= 1
            equiped += 1
        elif b > 0:
            fullPrice += arrpc2[pcounter]
            b -= 1
            equiped += 1
        pcounter += 1

print(str(equiped) + ' ' + str(fullPrice))
