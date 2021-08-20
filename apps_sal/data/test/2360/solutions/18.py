from time import time
t = int(input())
start_time = time()
for tt in range(t):
    n = int(input())
    stud = []
    for nn in range(n):
        s = tuple(map(lambda x: int(x), input().split()))
        stud.append(s)
    res = 0
    for i in range(n):
        (l, r) = stud[i]
        if i == 0:
            res = l + 1
            print(l, end=' ')
            continue
        newres = max(l, res)
        if newres > r:
            res = newres
            print(0, end=' ')
        else:
            print(newres, end=' ')
            res = newres + 1
    print()
