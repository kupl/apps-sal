nx = input().split()
for i in range(len(nx)):
    nx[i] = int(nx[i])
n = nx[0]
x = nx[1]
mas = input().split()
for i in range(len(mas)):
    mas[i] = int(mas[i])
mas.sort()
sum = 0
for i in mas:
    sum = sum + i * x
    if x > 1:
        x = x - 1
print(sum)
