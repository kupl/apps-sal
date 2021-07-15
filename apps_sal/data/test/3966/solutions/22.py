n=int(input())
lis=input().split()
for i in range(n):
    lis[i]=int(lis[i])
lis.sort()
m=max(lis)
s=0
for i in range(len(lis)):
   s+=lis[i]*(i+2) 
print(s-m)

