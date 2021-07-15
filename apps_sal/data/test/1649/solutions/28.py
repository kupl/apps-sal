ls = sorted(list(map(int, input().split())))

if ls[0] + ls[3] == ls[1] + ls[2]:
    print('Yes')
elif sum(ls[:-1]) == ls[-1]:
    print('Yes')
else:
    print('No')
