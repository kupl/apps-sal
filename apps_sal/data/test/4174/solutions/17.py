n,x = map(int, input().split())
a = [int(num) for num in input().split()]
sum = 0
cont = 1
for i in range(n):
    sum += a[i]
    if sum <= x:
        cont += 1
print(cont)
