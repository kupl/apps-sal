from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    lis = [[1]]

    now = []
    tmp = 0

    for i in range(1, n):
        if len(now) == 0:
            now.append(a[i])
            tmp = 1
        elif now[-1] > a[i]:
            if tmp == len(lis[-1]):
                lis.append(now)
                now = [a[i]]
                tmp = 1
            else:
                tmp += 1
                now.append(a[i])
        else:
            now.append(a[i])

    if len(now) > 0:
        lis.append(now)

    #print (lis)
    print(len(lis) - 1)
