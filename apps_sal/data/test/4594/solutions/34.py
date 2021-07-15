#85B
n=int(input())
data=[]
for i in range(0,n):
    data.append(int(input()))
res=sorted(data)
c=1
for j in range(1,n):
    if res[j]!=res[j-1]:
        c=c+1
print(c)
