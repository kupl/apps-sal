for _ in range(int(input())):
    n = int(input())
    arr = list([int(x)-1 for x in input().split()])
    l = -1
    r = -1
    for i in range(n):
        if arr[i] != i:
            if l == -1:
                l = i
            r = i+1
    if l == -1:
        print(0)
        continue
    ans = 1
    for i in range(l, r):
        if arr[i] == i:
            ans = 2
    print(ans)

