input()
a=list(map(int,input().split()))
b=[0]*5000
for x in a:
    b[x-1]+=1
r=''
count=0
max=0
for i in range(5000):
    if b[i]>0:
        count+=1
        max=i
        r+=str(i+1)+' ';
        b[i]-=1
for i in range(max-1,-1,-1):
    if b[i]>0:
        count+=1
        r+=str(i+1)+' ';
print(count)
print(r)
