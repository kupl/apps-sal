from math import sqrt
n=int(input())
a=0
m=0
while True:
    m+=1
    a=n*m+1
    for i in range(2,int(sqrt(a)+1)):
        if a%i==0:
            print(m)
            return

