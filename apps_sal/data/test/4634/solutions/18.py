for _ in range(int(input())):
    am = int(input())
    arr = list(map(int,input().split()))
    fl = False
    l = 0
    r = am
    for i in range(am):
        if arr[i] == 1:
            l = i
            break
    for i in range(am-1,-1,-1):
        if arr[i] == 1:
            r = i
            break
    print(arr[l:r].count(0))
