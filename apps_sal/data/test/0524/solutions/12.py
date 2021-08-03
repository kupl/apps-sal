n = int(input())
a = list(map(int, input().split()))

a.sort()
shita = int(a[-1]**(1 / (n - 1)))
ue = shita + 1

sumshita = 0
sumue = 0

for i in range(n):
    targetshita = shita**i
    sumshita += abs(targetshita - a[i])
    targetue = ue**i
    sumue += abs(targetue - a[i])

print(min(sumshita, sumue))
