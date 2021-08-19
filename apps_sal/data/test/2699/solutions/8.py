n = int(input())
a = [int(i) for i in input().split()]
for av in a:
    temp = []
    temp.append(1)
    for j in range(av - 1):
        temp.append(3 * 2 ** j + temp[-1])
    for v in temp:
        print(v, end=' ')
    print('\n', end='')
    temp1 = [i + 1 for i in temp]
    for v in temp1:
        print(v, end=' ')
    print('\n', end='')
    temp2 = [2 * i for i in temp1]
    for v in temp2:
        print(v, end=' ')
    print('\n', end='')
    dummy = []
    for k in range(len(temp)):
        dummy.append(temp2[k] - temp[k])
    for v in dummy:
        print(v, end=' ')
    print('\n', end='')
