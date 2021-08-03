from collections import Counter


def primfacs(n):
    if n % 2 == 0:
        primfac = [0, 0]
    else:
        primfac = [0, 0]
    while n % 2 == 0:
        n = n / 2
        primfac[0] += 1
    primfac[1] = n
    return primfac


t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    Ost = []
    for j in range(n):
        Ost.append(primfacs(A[j]))
    Ost.sort()
    d = {}
    for j in range(len(Ost)):
        d[Ost[j][1]] = Ost[j][0]
    print(sum(list(d.values())))
