t = int(input())
# a = list(map(int, input().split()))
for _ in range(t):
    n,x,y = map(int,input().split())
    
    
    for d in range(1,y-x+1):
        if (y-x)%d==0 and (y-x)//d <= (n-1):
            offset = y%d
            if offset==0:
                offset=d
            print(' '.join(map(str,(max(y,offset+(n-1)*d) - d*i for i in range(n)))))
            break
