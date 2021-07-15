t=int(input())
for tt in range(t):
    n,x,y=list(map(int,input().split()))
    mi = min(max(1, x + y - n + 1), n)
    k = n - ( 0 if x+y > n else n-x-y+1)
    print(mi, k)

