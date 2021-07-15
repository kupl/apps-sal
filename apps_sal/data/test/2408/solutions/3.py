import sys
input = sys.stdin.readline

n=int(input())
W=[list(map(int,input().split())) for i in range(n)]

SET=set()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def point(a,b,c,d):
    g=gcd(c-a,d-b)
    K=[(c-a)//g,(d-b)//g]

    if K==[0,1]:
        SET.add(tuple(K+[a]))

    else:
        SET.add(tuple(K+[((d-b)*(-a)+(c-a)*b)/(c-a)]))    

for i in range(n-1):
    a,b=W[i]
    for j in range(i+1,n):
        if i==j:
            continue
        c,d=W[j]

        point(a,b,c,d)

#print(SET)
LIST=list(SET)
ANS=0
for i in range(len(LIST)-1):
    NOW0,NOW1=LIST[i][0],LIST[i][1]
    for j in range(i+1,len(LIST)):
        if NOW0!=LIST[j][0] or NOW1!=LIST[j][1]:
            ANS+=1

print(ANS)

        
        
    

