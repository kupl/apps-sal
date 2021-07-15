a, b = list(map(int, input().split()))

lis = [4, 6, 9, 11]
lis2 = [1, 3, 5, 7, 8, 10, 12]

if a == b == 2:
    print('Yes')
elif a in lis and b in lis:
    print('Yes')
elif a in lis2 and b in lis2:
    print('Yes')
else:
    print('No')

