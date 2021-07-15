i=input()
l=[]
p=''
o=0
nuz=0
while o<len(i):
    p=i[o]
    if p >= 'a' and p <= 'z':
        if len(l)==0 or l[len(l)-1]!=p:
            l.append(p)
        else:
             l.pop()
             nuz+=1
    o+=1
if nuz%2==0:
    print('No')
else:
    print('Yes')

