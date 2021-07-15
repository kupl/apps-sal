import sys
import math

n,m,k=map(int,input().split())
jobs=[int(x) for x in input().strip().split()]
steve=jobs[:]
nade=steve[::-1]
suma,con,kik=0,0,0
for i in range(n):
    if(nade[i]>k):
        break
    if(suma+nade[i]<k):
        #print("A")
        suma+=nade[i]
        kik+=1
        if(i<n-1):
            if(suma+nade[i+1]>k):
                suma=0
                con+=1
    elif(suma+nade[i]==k):
        #print("B")
        #print("SPC CASE",suma,nade[i],suma+nade[i])
        con+=1
        kik+=1
        suma=0
    elif(suma+nade[i]>k):
        #print("C")
        con+=1
        suma=0
    #print(suma,kik)
    if(con>=m):
        break
print(kik)
