from sys import stdin
input = stdin.readline
n, p = list(map(int, input().split()))
c = list(map(int, input().split()))
dobre = []
for x in range(1, 2001):
    dobry = True
    miejsca = []
    for i in range(n):
        eps = max(c[i] - x, 0)
        cyk = max(n - eps, 0)
        miejsca.append(cyk)
    if min(miejsca) == 0:
        continue
    conajmniej = [0] * (n + 1)
    zajete = [0] * (n + 1)
    for i in miejsca:
        zajete[n - i] += 1
    sumapref = 0
    for i in range(n + 1):
        j = n - i
        sumapref += zajete[i]
        conajmniej[j] = sumapref
    for i in range(n):
        j = n - i
        if conajmniej[j] - i >= p or conajmniej[j] - i <= 0:
            dobry = False
            break
    if dobry:
        dobre.append(x)
print(len(dobre))
print(*dobre)
