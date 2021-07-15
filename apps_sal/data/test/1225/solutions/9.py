h = int(input())
sumn = 0
i,k = 0,1
while k <= h:
    sumn+=k
    i+=1
    k = 2**i
    
print(sumn)
