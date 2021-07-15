import sys
n=int(input())
#m=n//2*2
#twolist=[2**i for i in range(19)]

#for i in range(18,-1,-1):
#    if n>twolist[i]:
#        break

#for i in range((n+1)//2):
#    print(1)

#if n==3:
#    print(1,1,3)
#    return

i=0
ANS=[]
while n>0:
    if n==3:
        ANS=ANS+[2**i,2**i,3*2**i]
        break
    x=(n+1)//2
    ANS=ANS+[2**i]*x
    n=n-x
    i+=1
    
#ANS.append(m)

for a in ANS:
    print(a,end=" ")
    


