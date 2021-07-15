
# -*- coding: utf-8 -*-

def __starting_point():
    n  = int(input())
    a = list(map(int, input().split()))
    b = [0 for i in range(10)]
    pos = 1
    for i in range(n):
        b[a[i]-1]+=1
        c = []
        for j in range(10):
            if (b[j]>0):
                c.append(b[j])
        c.sort()
        if (c[len(c)-1]==i+1) or (c[len(c)-1]==c[len(c)-2]+1 and c[len(c)-2]==c[0])\
            or (c[len(c)-1]==c[1] and c[0]==1):
            pos = i+1
    print(pos)
__starting_point()
