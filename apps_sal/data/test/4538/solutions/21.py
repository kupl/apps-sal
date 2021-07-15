from math import sqrt,ceil
n,d=map(int,input().split())
count=0
for i in range(n):
    a,b=map(int,input().split())
    if(int(ceil(sqrt(pow(a,2)+pow(b,2))))<=d):
        count+=1
print(count)
