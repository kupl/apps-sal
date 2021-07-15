s=""
n=int(input())
if n==0:print(0)
else:
 while n!=0:s=str(n%2)+s;n=-(n//2)
 print(s)
