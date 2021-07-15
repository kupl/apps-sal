n,m,t3=map(int,input().split())
if (t3<n): 
      print(1+t3," ",1,sep="")
else:
      t3-=n
      if (m>=2):
            x=t3//(m-1)
            if x%2==0:
                  a=t3%(m-1) +2
                  b=n-x
            else:
                  a=(m-t3%(m-1))
                  b=n-x
            print(b,a)
      
