from sys import stdin
input = stdin.readline
n = int(input())
l = list(map(int, input().split()))
cyk = [1] * 50
for i in range(1, 50):
    cyk[i] = cyk[i - 1] * 2


def wyn(lista):
    m = max(lista)
    if m == min(lista):
        return 0
    le = len(bin(m))
    duze = []
    male = []
    pyk = cyk[le - 3]
    for i in lista:
        if i >= cyk[le - 3]:
            duze.append(i - pyk)
        else:
            male.append(i)
    if len(male) == 0:
        k = [lista[i] - pyk for i in range(len(lista))]
        return wyn(k)
    else:
        return pyk + min(wyn(duze), wyn(male))


print(wyn(l))
