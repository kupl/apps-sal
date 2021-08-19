import numpy as np


def resolve():
    # n=int(input())
    # a,b=map(int,input().split())
    # x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
    n, q = map(int, input().split())
    xe = np.array([0] * n)
    ye = np.array([0] * n)
    xemin, yemin = n - 1, n - 1
    bs = (n - 2)**2
    for i in range(q):
        j, x = map(int, input().split())
        if j == 1:
            if xemin >= x - 1:
                xe[x - 1:xemin] = yemin - 1
                xemin = x - 1
            bs -= xe[x - 1]
        else:
            if yemin >= x - 1:
                ye[x - 1:yemin] = xemin - 1
                yemin = x - 1
            bs -= ye[x - 1]
    print(bs)


def __starting_point():
    resolve()


__starting_point()
