import math
def find(n):
    if n==2:
        return 2
    for i in range(2,int(math.sqrt(n))+2):
        if n%i==0:
            return i
    return n
n=int(input())
lol=0
kek=2
while n>0:
    if n%2==0:
        lol+=n//2
        break
    f=find(n)
    lol+=1
    n-=f
print(lol)
