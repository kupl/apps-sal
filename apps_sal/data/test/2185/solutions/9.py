t = int(input())
for daf in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cs = 0
    f = True
    el = -1
    for i in range(n):
        if b[i] - a[i] < 0:
            f = False
            break
        if b[i] - a[i] != 0:
            if cs == 0:
                cs = 1
                el = b[i] - a[i]
            elif cs == 1:
                if b[i] - a[i] != el:
                    f = False
                    break
            else:
                f = False
                break
        else:
            if cs == 1:
                cs = 2
    if f:
        print("YES")
    else:
        print("NO")
