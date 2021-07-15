n1=int(input())
d1=list([int(x) for x in input().split(' ')])

n2=int(input())
d2=list([int(x) for x in input().split(' ')])


dl=list(set([0]+d1+d2))
dl.sort()

dd=dict()
for i in range(0,len(dl)):
    dd[dl[i]]=i

c1=[0 for i in range(0,len(dl))]
c2=[0 for i in range(0,len(dl))]

s1=[0 for i in range(0,len(dl))]
s2=[0 for i in range(0,len(dl))]

for d in d1:
    c1[dd[d]]+=1

for d in d2:
    c2[dd[d]]+=1

for i in range(len(dl)-2,-1,-1):
    s1[i]=s1[i+1]+c1[i+1]
    s2[i]=s2[i+1]+c2[i+1]

maxsub=s1[0]-s2[0]
maxi=0
maxa=s1[0]
for i in range(0,len(dl)):
    sub=s1[i]-s2[i]
    if sub>maxsub or (sub==maxsub and s1[i]>maxa):
        maxsub=sub
        maxa=s1[i]
        maxi=i

print(str(n1*2+s1[maxi])+':'+str(n2*2+s2[maxi]))


