import sys
n=int(input())
a=list(map(int,input().split()))
b=set()
beg=1
am=0
aml=[]
for i in range(n):
    if a[i] in b:
        aml.append([beg,i+1])
        am+=1
        b=set()
        beg=i+2
    else:
        b.add(a[i])
if am==0:
    print(-1)
    return
if aml[am-1][1]!=n:
    aml[am-1][1]=n
print(am)
for i in range(am):
    print(aml[i][0],aml[i][1])

