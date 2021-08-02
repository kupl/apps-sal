for _ in range(int(input())):
    a = [0] * 9
    for i in range(9):
        a[i] = list(input())
        a[i][a[i].index('2')] = '1'
        print(''.join(a[i]))
