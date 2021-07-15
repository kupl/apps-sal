import math

for i in range(int(input())):
    res = 'NO'
    n,d = list(map(int, input().split()))

    for x in range(0,100000):
        nd = x+math.ceil(d/(x+1))
        if nd <= n:
            res='YES'
    print(res)

