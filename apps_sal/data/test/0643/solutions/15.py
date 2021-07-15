for _ in range(int(input())):

  x,y,p,q=list(map(int,input().split()))

  l,r,res=0,10**18,-1

  while l<=r:

    mid=(l+r)//2

    a,b=p*mid-x,q*mid-y

    if a<=b and a>-1 and b>-1:res=b;r=mid-1

    else :l=mid+1

  print(res)



# Made By Mostafa_Khaled

