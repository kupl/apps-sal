n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = sorted(a)
if n == 0:
    b = [1, 1, 3, 3]
elif n == 1:
    b = [a[0], a[0] * 3, a[0] * 3]
elif n == 2:
    if a[0] == a[1]:
        b = [a[1] * 3, a[1] * 3]
    elif a[0] * 3 >= a[1]:
        b = [a[0] * 3, a[0] * 4 - a[1]]
    else:
        b = None
elif n == 4:
    if a[0] * 3 == a[3] and a[0] * 4 == a[1] + a[2]:
        b = []
    else:
        b = None
elif a[0] * 3 >= a[2] and a[0] * 4 == a[1] + a[2]:
    b = [a[0] * 3]
elif a[0] * 3 == a[2]:
    b = [a[0] * 4 - a[1]]
elif a[2] * 4 / 3 == a[0] + a[1]:
    b = [a[2] // 3]
else:
    b = None
if b == None:
    print('NO')
else:
    print('YES')
    for x in b:
        print(x)
