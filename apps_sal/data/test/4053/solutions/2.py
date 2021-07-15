n=int(input())
AB=[input() for i in range(2*n-2)]

ABSORT=sorted(AB,key=lambda x:len(x),reverse=True)

CANDI=[]

if ABSORT[0][1:]==ABSORT[1][:-1]:
    CANDI.append(ABSORT[0]+ABSORT[1][-1])

if ABSORT[1][1:]==ABSORT[0][:-1]:
    CANDI.append(ABSORT[1]+ABSORT[0][-1])

if CANDI[0]==CANDI[-1]:
    CANDI=[CANDI[0]]

for c in CANDI:
    for s in AB:
        ls=len(s)

        if c[:ls]==s or c[-ls:]==s:
            continue
        else:
            break
    else:
        DE=c
        break


DEAB=[(AB[i],i) for i in range(2*n-2)]
DEAB.sort(key=lambda x:len(x[0]))

ANSLIST=[None]*(2*n-2)
for i in range(n-1):
    s,si=DEAB[2*i]
    t,ti=DEAB[2*i+1]
    ls=len(s)

    if DE[:ls]==s and DE[-ls:]==t:
        ANSLIST[si]="P"
        ANSLIST[ti]="S"
    else:
        ANSLIST[si]="S"
        ANSLIST[ti]="P"

for a in ANSLIST:
    print(a,end="")

print()



