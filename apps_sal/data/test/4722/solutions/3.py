a = list(map(int, input().split()))
b = sum(a)

if (b % 3 == 0 or a[0] % 3 == 0 or a[1] % 3 == 0):
    print('Possible')
else:
    print('Impossible')
