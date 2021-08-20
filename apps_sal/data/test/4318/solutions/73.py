n = int(input())
a = list(map(int, input().split()))
cont = 1
h = a[0]
for i in range(1, n):
    if a[i] >= h:
        h = a[i]
        cont += 1
print(cont)
