import math
s,p=map(int,input().split())
l=[]
for i in range(1,int(math.sqrt(p))+1):
    if p%i==0:
        l.append(i)
for i in l:
    j=p//i
    if i+j==s:
        print("Yes")
        return
print("No")
