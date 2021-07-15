import sys
input = sys.stdin.readline
t=int(input())
while t>0:
    t-=1
    n,ss=map(int,input().split())
    lr=[]
    sl=0
    for i in range(n):
        l,r=map(int,input().split())
        sl+=l
        lr.append([l,r])
        
    l=0
    r=10**9+1
    while r-l>1:
        mid=(r+l)//2
        s=[]
        for i in range(n):
            if mid<=lr[i][1]:
                s.append(max(-lr[i][0],-mid))
                
        if len(s)<n//2+1:
            r=mid
            continue
        s.sort()
        sumi=sl+(n//2+1)*mid+sum(s[:n//2+1])
       
        if sumi>ss:
            r=mid
        else:
            l=mid
        #print(r,l)
        #print(r,l,sumi,ss)    
    print(l)    
