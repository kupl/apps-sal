a = list(map(int, input().split()))
if abs(a[1] - a[0]) <= a[3] and abs(a[2] - a[1]) <= a[3] or abs(a[2] - a[0]) <= a[3]:
    print('Yes')
else:
    print('No')
