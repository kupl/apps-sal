t = int(input())
while(t):
    t -= 1
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    p = set(p)
    for i in range(n):
        for j in range(0, n - i - 1):
            if(a[j] > a[j + 1] and j + 1 in p):
                a[j], a[j + 1] = a[j + 1], a[j]
    flag = 0
    mi = -1000
    for i in range(n):
        if(mi <= a[i]):
            mi = a[i]
            continue
        flag = 1
    if(flag == 1):
        print("NO")
    else:
        print("YES")
