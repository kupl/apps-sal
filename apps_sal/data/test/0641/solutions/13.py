a = list(input().split())
if a[2] == 'month':
    if a[0] == '31':
        print(7)
    elif a[0] == '30':
        print(11)
    else:
        print(12)
else:
    if a[0] == '5' or a[0] == '6':
        print(53)
    else:
        print(52)
