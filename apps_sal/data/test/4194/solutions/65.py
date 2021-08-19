a = input().split()
b = input().split()
suma = 0
for x in range(int(a[1])):
    suma += int(b[x])
dias = int(a[0]) - suma
if dias < 0:
    print('-1')
else:
    print(dias)
