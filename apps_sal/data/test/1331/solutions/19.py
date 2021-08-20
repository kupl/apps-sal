(n, m, k) = [int(x) for x in input().split()]
alarms = [int(x) for x in input().split()]
alarms.sort()
al2 = []
cont = 0
for i in range(len(alarms)):
    al2.append(alarms[i])
    if len(al2) >= k and al2[-1] - al2[len(al2) - k] < m:
        al2.pop()
        cont += 1
print(cont)
