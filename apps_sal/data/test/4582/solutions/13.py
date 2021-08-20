(a, b) = input().split()
if a == 'H':
    print(b)
elif a == 'D':
    print('HD'[int(not 'HD'.index(b))])
