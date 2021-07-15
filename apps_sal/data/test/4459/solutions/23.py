from collections import Counter
n=int(input())
L=Counter(list(map(int,input().split())))
ans=0
for i in L:
    if i!=L[i]:
        if L[i]-i>0:
            ans=ans+L[i]-i
        else:ans+=L[i]
print(ans)

