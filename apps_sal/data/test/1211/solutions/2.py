n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
mn = 10 ** 20
a1, a2 = 1, 0
for i in range(k):
    if n % a[i] < mn:
        mn = n % a[i]
        a1 = i + 1
        a2 = n // a[i]
print(a1, a2)
