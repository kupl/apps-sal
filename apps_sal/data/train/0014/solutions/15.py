T = int(input())

for t in range(T):
    i1 = [int(i) for i in input().split(' ')]
    i2 = [int(i) for i in input().split(' ')]
    if i1[0] == i2[0] and i1[1] + i2[1] == i1[0]:
        print('Yes')
    elif i1[0] == i2[1] and i1[1] + i2[0] == i1[0]:
        print('Yes')
    elif i1[1] == i2[0] and i1[0] + i2[1] == i1[1]:
        print('Yes')
    elif i1[1] == i2[1] and i1[0] + i2[0] == i1[1]:
        print('Yes')
    else:
        print('No')
