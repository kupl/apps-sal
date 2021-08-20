a = [int(i) for i in input().split()]
if a[0] == a[1] and a[0] != a[2] or (a[0] == a[2] and a[0] != a[1]) or (a[2] == a[1] and a[2] != a[0]):
    print('Yes')
else:
    print('No')
