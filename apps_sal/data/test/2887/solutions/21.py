n = int(input())
soup = list(map(int, input().split()))
evap = list(map(int, input().split()))
for i in range(n):
    summ = 0
    for j in range(i + 1):
        if soup[j] >= evap[i]:
            summ += evap[i]
            soup[j] -= evap[i]
        else:
            summ += soup[j]
            soup[j] = 0
    print(summ, end=' ')
