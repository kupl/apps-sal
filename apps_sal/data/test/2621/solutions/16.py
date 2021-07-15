t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    h = list(map(int,input().split()))
    b = False
    for i in range(n-1):
        m += h[i] - max(h[i+1]-k,0)
        if m < 0:
            b = True
            break
    if b:
        print("NO")
    else:
        print("YES")
