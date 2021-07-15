def f():
 t=int(input())
 while t>0:
  t-=1
  n,b=map(int,input().split())
  if b>=n:
   print(n)
  else:
   if n%b==0:
    ans=((n//b)-1)*(b-1)+b
    print(ans)
   else:
    ans=(((n-1)//b)-1)*(b-1)+b+((n-1)%b)
    print(ans)
f()
