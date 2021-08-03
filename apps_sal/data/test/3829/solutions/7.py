m, n = list(map(int, input().split(' ')))
sumx = 0
for i in range(1, m + 1):
    sumx += i * ((i / m)**n - ((i - 1) / m)**n)
print(sumx)
