n=int(input())
a=[]
a=[int(x) for x in input().split()]
c=1
max1=0
for i in range(1,len(a)):
    if a[i]>=a[i-1]:
        c=c+1
    else:
        if c>max1:
            max1=c
        c=1
if c>max1:
    max1=c
print(max1)        

