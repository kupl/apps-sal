a = list(map(int, input().split()))
a.sort()
if a[0] + a[3] == a[1] + a[2]:
    print('Yes')
elif a[0] + a[1] + a[2] == a[3]:
    print('Yes')
else:
    print('No')
