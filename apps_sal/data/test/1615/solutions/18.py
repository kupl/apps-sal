n,k=map(int,input().split())
L={""}
for i in range(n):
   m,f=input().split()
   for i in range (int(m),int(f)+1):
      L |= {i}
L.remove("")
x=len(L)
i=0
while x%k!=0:
   x+=1
   i+=1
print(i)
