n=int(input())
L=[]
Startswith=[]
for i in range(n):
    L.append(input())
    Startswith.append(L[i][0])

Cases=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
coeff=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in L :
    n=len(i)
    for j in range(n):
        coeff[Cases.index(i[j])]+=10**(n-j-1)

cof=list(coeff)
t=False
k=0
while((len(cof)!=0) and (t==False)):
    m=max(cof)
    p=cof.index(m)
    if ( Cases[p]  in Startswith ) :
        cof[p]=-1
        
    else :
        
        t=True
        coeff[p]=-1
        Cases[p]=0

c=max(coeff)
j=1
while (len(coeff)!=0 and(c!=-1)):
    c1=coeff.index(c)
    coeff[c1]=-1
    Cases[c1]=j
    j+=1
    c=max(coeff)


def convert(ch,Cases):
    n=len(ch)
    s=0
    for i in range(n):
        s+=(10**(n-i-1))*Cases[ord(ch[i])-97]
    return(s)

L=[convert(i,Cases) for i in L ]
print(sum(L))
                             

