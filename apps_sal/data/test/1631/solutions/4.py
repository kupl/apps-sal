n=int(input())
x=input()
a=len(x)
lex=dict()
ALPHA=list('abcdefghijklmnopqrstuvwxyz')

for i in ALPHA:
    for j in ALPHA:
        lex[(i,j)]=0
    
for i in range(n-1):
    y=input()
    b=len(y)
    for j in range(min([a,b])):
        if x[j]!=y[j]:
            if lex[(x[j],y[j])]==-1:
                print('Impossible')
                raise SystemExit
            else:
                lex[(x[j],y[j])]=1
                lex[(y[j],x[j])]=-1
                x=y
                a=b
            break
        if j==(min([a,b])-1):
            if a>b:
                print('Impossible')
                raise SystemExit
            x=y
            a=b
    
def biggest(alphabet):
    for i in alphabet:
        t=0
        for j in alphabet:
            if lex[(i,j)]<0:
                t=1
                break
        if t==0:
            return i
    return -1
newalpha=['']*26 
i=0
while ALPHA!=[]:
    BIG=biggest(ALPHA)
    if biggest(ALPHA)==-1:
        print('Impossible')
        raise SystemExit
    newalpha[i]=BIG
    i=i+1
    ALPHA.remove(BIG)

print(''.join(newalpha))
    

        

