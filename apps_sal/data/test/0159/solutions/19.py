import math
n=int(input())
mas=[int(c) for c in  input().split()]
l=[]
m=mas[0]
for i in range(n-1):
    if math.gcd(mas[i],mas[i+1])!=1:
        l.append(i+1)
       # print(l)
for i in l[::-1]:
    mas.insert(i,1)
k=len(mas)-n
print(k)
for i in mas:
    print(i,end=' ')


