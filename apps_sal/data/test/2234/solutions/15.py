import math as mt
def tran(arr):
    if arr[1]>arr[0]:
        return arr[1]-arr[0]
    else:
        if arr[1]%2==0:
            if arr[0]%2==0:
                return 0
            else:
                return 1
        else:
            if arr[0]%2==1:
                return 0
            else:
                return 1

def __starting_point():
    t = int(input())
    ans = []
    for i in range(t):
        arr = list(map(int, input().rstrip().split()))
        r = tran(arr)
        ans.append(r)
    for i in ans:
        print(i)

__starting_point()
