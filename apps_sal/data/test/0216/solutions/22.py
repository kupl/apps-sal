n = int(input())
a = list(map(int, input().split(' ')))
sumv = 0
for i in range(n):
    if a[i] < 0:
        sumv -= a[i]
    else:
        sumv += a[i]
print(sumv)
