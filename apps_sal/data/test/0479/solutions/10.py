n_k = input()
n_k = n_k.split(" ")

n = int(n_k[0])
k = int(n_k[1])

ais = input()
ais = ais.split(" ")

q = int(input())

pares = {}

for a in ais:
    a = int(a)
    for i in range(k):
        p = int((i + 1) * a)
        if (p not in pares) or (i + 1 < pares[p]):
            pares[p] = i + 1

m = 1000000000

for i in range(q):
    x = int(input())
    ans = 1000;

    minimo = m
    for money, bills in list(pares.items()):
        if money == x and bills <= k and bills < minimo:
            minimo = bills
        else:
            r = x - money
            if r in pares and bills + pares[r] < minimo and bills + pares[r] <= k:
                minimo = bills + pares[r]
    if minimo == m:
        print(-1)
    else:
        print(minimo)
