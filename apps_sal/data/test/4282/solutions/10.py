n = int(input())
mas = []
itog = []
for i in range(n):
    a = list(map(int, input().split()))
    mas.append(a)
itog.append(1)
p = 0
while len(itog) < n - 1:
    if (mas[p][1] in mas[mas[p][0] - 1]):
        itog.append(mas[p][0])
        p = mas[p][0] - 1
    else:
        itog.append(mas[p][1])
        p = mas[p][1] - 1

if (mas[p][1] in mas[mas[p][0] - 1]) and not(mas[p][0] in itog):
    itog.append(mas[p][0])
    p = mas[p][0] - 1
else:
    itog.append(mas[p][1])
    p = mas[p][1] - 1

for i in itog:
    print(i, end=" ")
