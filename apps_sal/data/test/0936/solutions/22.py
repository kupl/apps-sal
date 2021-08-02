n = int(input())
line = input().split()
maxi = line[0]
mas = {}
mas[maxi] = 1
for i in range(1, n):
    a = line[i]
    if not a in mas:
        mas[a] = 1
    else:
        mas[a] += 1
    if (mas[a] > mas[maxi]):
        maxi = a
print(maxi)
