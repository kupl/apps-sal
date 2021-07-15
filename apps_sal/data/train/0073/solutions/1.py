# Fast IO (only use in integer input) or take care about string

# import os,io
# input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    operation = []
    while True:
        isNonDecreasing = True
        for i in range(n-1):
            if a[i] > a[i+1]:
                isNonDecreasing = False
                break
        if isNonDecreasing:
            break
        isNIn = [False] * (n + 1)
        for elem in a:
            isNIn[elem] = True
        for i in range(n + 1):
            if isNIn[i] == False:
                MEX = i
                break
        if MEX == n:
            for i in range(n):
                if a[i] != i and a[i] != n:
                    break
            operation.append(str(i + 1))
            a[i] = n
        else:
            operation.append(str(MEX+1))
            a[MEX] = MEX
    print(len(operation))
    if len(operation) != 0:
        print(' '.join(operation))

