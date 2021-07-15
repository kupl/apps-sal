n,m,k=map(int,input().split())
if (k<n):
      print(k+1," ",1,sep="")
else:
      k-=n
      if (m>=2):
            x=k//(m-1)
            if x%2==0:
                  a=k%(m-1) +2
                  b=n-x
            else:
                  a=(m-k%(m-1))
                  b=n-x
            print(b,a)
      

