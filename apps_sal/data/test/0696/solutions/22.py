from fractions import gcd

tt=0

#phi(p-1)

x=int(input())

x-=1

for i in range(1, x+1):

    if gcd(x,i)==1:

        tt+=1

print(tt)


