import math
def combi(L,n):
    return math.factorial(L)//math.factorial(n)//math.factorial(L-n)


T=int(input())
LR=[list(map(int,input().split())) for i in range(T)]

def classy(less,nonzero,now):
    L=len(str(now))

    if less==0:
        if 3-nonzero>=L:
            return 10**L
        else:
            ANS=1
            for i in range(1,3-nonzero+1):
                ANS+=combi(L,i)*(9**i)

            return ANS

    else:
        if nonzero<=2:
            if now<=9:
                return now+1
            
            else:
                if int(str(now)[0])==1:
                    return classy(1,nonzero+1,int(str(now)[1:]))\
                           +classy(0,nonzero,int("9"*(L-1)))\

                else:
                    return classy(1,nonzero+1,int(str(now)[1:]))\
                           +(int(str(now)[0])-1)*classy(0,nonzero+1,int("9"*(L-1)))\
                           +classy(0,nonzero,int("9"*(L-1)))

        else:
            return 1

for l,r in LR:
    print(classy(1,0,r)-classy(1,0,l-1))

            
        
                          
        
    
    

