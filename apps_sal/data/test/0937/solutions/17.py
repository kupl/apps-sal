(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
bodr = [int(x) for x in input().split()]
su = 0
for i in range(n):
    if bodr[i]:
        su += a[i]
        a[i] = 0
summa = sum(a[:k])
head = 0
maxi = summa
for i in range(k, n):
    summa -= a[head]
    head += 1
    summa += a[i]
    maxi = max(summa, maxi)
print(su + maxi)
