def index(l):
    for i in range(n):
        if l[i]>0:
            j=(i+1)-l[i]
            l1.append(j)
    return(l1)
n=int(input())
hand=[int(g) for g in input().split()]
deck=[int(g) for g in input().split()]
if 1 in deck:
    index2=deck.index(1)
l1=[]
buffer=deck[:]
buffer.sort()
l2=index(deck)
if len(set(deck))==1 and set(deck)=={0}:
    output=(n)
elif 0 not in deck and deck==buffer:
    output=(0)
elif 1 in deck :
    if index2==0:
        output=(max(l2)+n+1)
    if set(deck[:index2])=={0}:
        li=[int(g) for g in range(1,n-index2+1)]
        if deck[index2:]==li:
            output=index2
        else:
            output=(max(l2)+n+1)
    else:
        for i in range(index2):
            if deck[i]>0:
                if (index2-i)>=(n-deck[i])+2:
                    output=(l2[-1])
                else:
                    output=(max(l2)+n+1)
                    break
else:
    if max(l2)<=(-1):
        output=(n)
    else:
        output=(max(l2)+n+1)
print(output)
    

