n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
suma = 0
sumb = 0
for x in a:
    suma += x
for x in b:
    sumb += x
print("Yes" if suma >= sumb else "No")
