n = int(input())
a = [int(x) for x in input().split()]
for i in range(len(a)):
    if a[i] % 2 == 0 and a[i] > 0:
        a[i] = 2
    if a[i] % 2 == 1:
        a[i] = 1
possible = True
for i in range(len(a)):
    if a[i] == 1:
        if i + 1 < len(a) and a[i + 1] > 0:
            a[i] = 0
            a[i + 1] -= 1
for i in range(len(a)):
    if a[i] == 1:
        possible = False
if possible:
    print('YES')
else:
    print('NO')
