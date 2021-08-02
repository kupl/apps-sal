def buscaEnergia(perna, qtd):
    total = 0
    if(qtd == 0):
        return total
    for i in range(len(d) - 1, -1, -1):
        for v in d[i]:
            if(v < perna):
                qtd -= 1
                total += i
            else:
                break
            if(qtd == 0):
                break
        if(qtd == 0):
            break
    return total


n = int(input())
tamanhoPerna = [int(i) for i in input().split()]
energiaPerna = [int(i) for i in input().split()]
d = [[] for i in range(201)]
cntPerna = [0] * 100001
sumPerna = [0] * 100001
corteTotal = 0
maxTam = 0

for i in range(len(tamanhoPerna)):
    d[energiaPerna[i]].append(tamanhoPerna[i])
    sumPerna[tamanhoPerna[i]] += energiaPerna[i]
    cntPerna[tamanhoPerna[i]] += 1
    corteTotal += energiaPerna[i]
    maxTam = max(tamanhoPerna[i], maxTam)

for i in range(len(d)):
    d[i].sort()

currentMin = float("inf")
for perna in tamanhoPerna:
    somaMesa = sumPerna[perna]
    somaMesa += buscaEnergia(perna, cntPerna[perna] - 1)
    currentMin = min(currentMin, corteTotal - somaMesa)
print(currentMin)
