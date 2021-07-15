n,k=[int(x) for x in input().split()]
if k==1:
   print(n)
   return
a=1
s=0
while a<=n:
   s+=a
   a*=2
print(s)

