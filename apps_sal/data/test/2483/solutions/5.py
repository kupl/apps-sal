n,c=list(map(int,input().split()))
table=[0]*220000
chanels=[[]for i in range(c)]
for i in range(n):
    a,s,ch=list(map(int,input().split()))
    chanels[ch-1].append((a,s))
for i in range(c):
    if chanels[i]:
        chanels[i].sort()
        x,y=chanels[i][0]
        for p,q in chanels[i][1:]+[(0,0)]:
            if y==p:y=q
            else:
                table[2*x-1]+=1
                table[2*y]-=1
                x,y=p,q

from itertools import accumulate
print((max(list(accumulate(table)))))

