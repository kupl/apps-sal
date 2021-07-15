n=int(input())
lis=input().split()
for i in range(n):
    lis[i]=int(lis[i])
count=[0,0,0]
lis1=[]
lis2=[]
lis3=[]
for i in range(n):
    if lis[i]==1:
        count[0]+=1
        lis1.append(i)
    if lis[i]==2:
        count[1]+=1
        lis2.append(i)
    if lis[i]==3:
        count[2]+=1
        lis3.append(i)
if min(count)==0:
    print(0)
else:
    print(min(count))
    for i in range(min(count)):
        print(lis1[i]+1,lis2[i]+1,lis3[i]+1)

