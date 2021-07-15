import sys
input = sys.stdin.readline

n,k=list(map(int,input().split()))

"""
if (k<=50 and n>2**k-1) or n<k*(k+1)//2:
    print("NO")

else:
    print("YES")
"""

ANS=list(range(1,k+1))
ANS.append(10**9)
SUM=k*(k+1)//2
PLUS=0

for i in range(k):
    if n<SUM:
        print("NO")
        return

    y=2*ANS[i-1]-ANS[i]
        
    x=min((n-SUM)//(k-i),y-PLUS)
    #print(i,x)
    SUM+=x*(k-i)
    PLUS+=x
    ANS[i]=ANS[i]+PLUS

if sum(ANS[:k])==n:
    print("YES")
    print(*ANS[:k])
else:
    print("NO")
    


