x = int(input())
m = 2 * (10**5)
lis = [True for i in range(m)]
i = 2
while i * i <= m:
    if lis[i]:
        for j in range(2 * i, m, i):
            lis[j] = False
    i += 1
while True:
    if lis[x]:
        print(x)
        break
    x += 1
