import math as mt


def tran(arr):
    if arr[0] == 0 or arr[1] == 0 or arr[2] == 0:
        o = 0
        for i in arr:
            if i % 2 == 1:
                o += 1
        if o > 1:
            return 'No'
        else:
            return 'Yes'
    else:
        o = 0
        for i in arr:
            if i % 2 == 1:
                o += 1
        if o == 2:
            return 'No'
        else:
            return 'Yes'


def __starting_point():
    t = int(input())
    ans = []
    for i in range(t):
        nk = list(map(int, input().rstrip().split()))
        r = tran(nk)
        ans.append(r)
    for i in ans:
        print(i)


__starting_point()
