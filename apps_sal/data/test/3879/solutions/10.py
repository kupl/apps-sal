n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
    while a[i] % 2 == 0:
        a[i] /= 2
    while a[i] % 3 == 0:
        a[i] /= 3
print('Yes' if all((x == a[0] for x in a)) else 'No')
