n = int(input())
b = True
a = [int(i) for i in input().split()]
for i in range(n - 1):
    if abs(a[i + 1] - a[i]) >= 2:
        b = False
if b:
    print('YES')
else:
    print('NO')
