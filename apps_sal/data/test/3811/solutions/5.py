import math
import sys
def printDivisors(n,dict1) :
    i=2
    while i <= math.sqrt(n):
         
        if (n % i == 0) :
            if (n // i == i) :
                dict1[i]=1
            else :
                dict1[i]=1
                dict1[n//i]=1

        i = i + 1
    dict1[n]=1
f=sys.stdin

n=int(f.readline().rstrip('\r\n'))
minval=2000000000000
x1=-1
y1=-1
dict2={}
for i in range(n):
    x,y=map(int,f.readline().rstrip('\r\n').split())
    dict2[(x,y)]=1
    if(x+y<minval):
        minval=x+y
        x1=x
        y1=y
dict1={}
printDivisors(x1,dict1)
printDivisors(y1,dict1)
flagx=0
for i in dict2.keys():
    flag=0
    k1=dict1.keys()
    dict1={}
    for j in k1:
        if(i[0]%j==0 or i[1]%j==0):
            dict1[j]=1
            flag=1
    if(flag==0):
        flagx=1
        break 
if(flagx==1):
    print(-1)
else:
    for i in dict1.keys():
        print(i)
        break
