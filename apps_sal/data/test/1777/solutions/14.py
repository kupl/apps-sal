import sys
input = sys.stdin.readline

n=int(input())
B=[input().strip() for i in range(n)]

LIST=[]

for b in B:
    care=0

    BRSUM=0
    for bb in b:
        if bb==")":
            BRSUM-=1
        else:
            BRSUM+=1

        if BRSUM<0:
            care=min(care,BRSUM)

    if care<0 and BRSUM>care:
        continue
    else:
        LIST.append(BRSUM)

from collections import Counter
counter=Counter(LIST)

ANS=0
for l in sorted(list(counter.keys())):
    if l==0:
        ANS+=counter[l]//2
        break
    
    if l>0:
        break

    ANS+=min(counter[l],counter[-l])


print(ANS)

        

