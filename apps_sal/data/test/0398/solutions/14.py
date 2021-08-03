n = int(input())
a = [int(el) for el in input().split()]

a.sort()
for i in range(n - 2):
    b, c, d = a[i], a[i + 1], a[i + 2]
    if b + c > d:
        print('YES')
        break
else:
    print('NO')
