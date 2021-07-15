n=int(input())
a=int(input())
s=a
for i in range(n-1):
   b=int(input())
   s+=abs(b-a)
   a=b
print(s+2*n-1)

