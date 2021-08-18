n, k = map(int, input().split())
a = [input() for i in range(n + 1)]
z = 0
for i in a:
    if i == '?':
        z += 1
if k == 0:
    if a[0] == '0':
        print('Yes')
    elif a[0] == '?' and (n - z + 1) % 2 == 1:
        print('Yes')
    else:
        print('No')
else:
    if z == 0:
        d = 0
        for i in a[::-1]:
            d = (d * k + int(i)) % 7272763523821
        if d == 0:
            print('Yes')
        else:
            print('No')
    else:
        if n % 2 == 0:
            print('No')
        else:
            print('Yes')
