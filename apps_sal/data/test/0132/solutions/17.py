kolichestvoKuskov = int(input())
spisokUglov = list(map(int, input().split()))
raznica = 180
for a in range(0, kolichestvoKuskov):
    sum = 0
    for i in range(a, kolichestvoKuskov):
        sum += spisokUglov[i]
        if raznica > abs(180 - sum):
            raznica = abs(180 - sum)
print(raznica * 2)
