def resolve():
    n = int(input())
    h = list(map(int,input().split()))
    ans = 'Yes'
    for i in range(0,n-1):
        if h[n-i-1] >= h[n-i-2]:
            continue
        elif h[n-i-1]-h[n-i-2]==-1:
            h[n-i-2] -= 1
        else:
            ans = 'No'
    print(ans)
resolve()
