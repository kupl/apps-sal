
a,b,c=list(map(int,input().split()))
d=[a,b,c]

min1=0
d.sort()    
[a,b,c]=d
while(a+b<=c):
    a+=1
    min1+=1
print(min1)


