n, k = [int(z) for z in input().split()]
a = [int(z) for z in input().split()]
best = 10000000000000000000
for i in range(k):
    if (n % a[i]) < best:
        best = n % a[i]
        num = n // a[i]
        kor = i + 1
print(kor, num)
