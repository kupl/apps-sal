import math
K=int(input())

list1=[]
s=1
while s<=K:
    list1.append(s)
    s=s+1

list3=[]
t=1
while t<=K*K:
    list3.append(t)
    t=t+1

list2=[]
k=1
for i in list1:
    for j in list1:
        X=math.gcd(i,j)
        list2.append(X)

Y=0
for k in list1:
    for l in list3:
        Y=Y+math.gcd(k,list2[l-1])

print(Y)

