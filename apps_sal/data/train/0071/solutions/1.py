
T = int(input())

#lets = 'abcdefghijklmnopqrstuvwxyz'
#key = {lets[i]:i for i in range(26)}

for t in range(T):
    n = int(input())
    #n,k = map(int,input().split())
    a = list(map(int, input().split()))
    #a = input().split()
    d = False
    cu = 0
    cu_m = 0
    for i in range(n):
        cu += a[i]
        cu_m = min(cu_m, cu)

    print(-cu_m)
