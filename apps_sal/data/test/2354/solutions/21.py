import sys



n,q=map(int,sys.stdin.readline().strip().split())
nc=n
# print(n,q)
    
if(n%2==0):
    n2=int((n*n)/2)
else:
    n2=int((n*n)/2)+1
n1=int(n/2)
if(1==1):
    for i in range(q):
        x,y=map(int,sys.stdin.readline().strip().split())
        # print(n,q,x,y)
        x1=int(x/2)
        y1=int(y/2)
        op=0
        if(x%2!=0):
        
            if(y%2!=0):
                if(x>1):
                    op=n*(x1)
                op=op+1+(y1)
            else:
                op=n2+(n*x1)+y1
    
        else:
            if(y%2==0):
                if(n%2==0):
                    op=n1
                else:
                    op=n1+1
                op=op+(n*(x1-1))
                op=op+y1
    
            else:
                
                op=n2+n1+(n*(x1-1))+(y1)+1
        print(op)
