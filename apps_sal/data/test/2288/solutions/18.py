for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = []
    y = []
    for i in range(n):
        if b[i] == 0:
            x.append(a[i])
        else:
            y.append(a[i])
    if len(x) == 0:
        if y == sorted(y):
            print("Yes")
        else:
            print("No")
    elif len(y) == 0:
        if x == sorted(x):
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
        '''
        x.sort()
        y.sort()
        merged = []
        i = 0
        j = 0
        for elem in b:
            if elem == 0:
                merged.append(x[i])
                i += 1
            else:
                merged.append(y[j])
                j += 1
        if merged == sorted(merged):
            print("Yes")
        else:
            print("No")
'''
