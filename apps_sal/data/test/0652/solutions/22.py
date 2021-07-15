n=int(input())
l=[]
l1=[1]*(n**2)
ans=0
for i in range(n):
    x,y=input().split()
    x,y=[int(x),int(y)]
    l.append([x,y])

from collections import Counter
count=Counter()
for i in range(len(l)):
    
    for j in range(i+1,len(l)):
        
        count[l[i][0]+l[j][0],l[j][1]+l[i][1]]+=1
ans = sum(i * (i - 1) // 2 for i in list(count.values()))
print(ans)

