
# -*- coding: utf-8 -*-

def __starting_point():
    n, z = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, z)
    a.sort()
    # print(a)
    mask = [0 for i in range(n)]
    start = int((n-1)/2)
    end = n - 1
    res = 0
    while end>=0:
        if abs(a[start]-a[end])>=z and mask[end]==0 and mask[start]==0:
            mask[start] = 1
            mask[end] = 1
            # print("start: {}, a[start]: {}, end: {}, a[end]: {}".\
            #     format(start, a[start], end, a[end]))
            start -= 1
            end -= 1
            res += 1 
        else:
            if (mask[start]==1):
                start -= 1
            elif mask[end]==1:
                end -= 1
            else:
                start -= 1
        if start<0:
            break
            
    print(res)
__starting_point()
