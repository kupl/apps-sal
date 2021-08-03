n = int(input())
a = list(map(int, input().split()))

aux = 0
minaux = 0
maxim = 0
results = []

for i in range(1, n):
    results.append(abs(a[i - 1] - a[i]))


for i in range(0, n - 1):
    if i % 2 == 1:
        condition = -results[i]
    else:
        condition = results[i]
    aux += condition
    minaux -= condition
    if aux > maxim:
        maxim = aux
    if condition > maxim:
        maxim = condition
    if minaux > maxim:
        maxim = minaux
    if minaux < 0:
        minaux = 0
    if aux < 0:
        aux = 0

print(maxim)
