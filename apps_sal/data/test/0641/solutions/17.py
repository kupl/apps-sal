a = list(map(str, input().split()))
a[0] = int(a[0])
if a[2] == 'month':
    if a[0] <= 29:
        print(12)
    elif a[0] == 30:
        print(11)
    else:
        print(7)
else:
    if a[0] >= 5 and a[0] != 7:
        print(53)
    else:
        print(52)

