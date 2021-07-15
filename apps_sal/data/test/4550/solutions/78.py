x = list(map(int, input().split(' ')))
if x[0] == x[1] + x[2]:
    print('Yes')
elif x[0] + x[1] == x[2]:
    print('Yes')
elif x[0] + x[2] == x[1]:
    print('Yes')
else:
    print('No')
