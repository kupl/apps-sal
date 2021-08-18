
T = int(input())


for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    d = False
    cu = 0
    cu_m = 0
    for i in range(n):
        cu += a[i]
        cu_m = min(cu_m, cu)

    print(-cu_m)
