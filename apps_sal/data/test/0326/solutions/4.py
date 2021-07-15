import sys
input = sys.stdin.readline

N=int(input())
ST=[input().split() for i in range(N)]

for i in range(N):
    ST[i][1]=int(ST[i][1])

ST.sort()

ST2=[]
for i in range(N):
    if i>0 and ST[i][0]==ST[i-1][0]:
        continue
    ST2.append((ST[i][0],ST[i][1]))
ST=ST2


FDICT=dict()
BDICT=dict()

for s,i in ST:
    FDICT[s[::-1]]=i
    BDICT[s[::-1]]=i

    for j in range(1,len(s)):
        if not(s[:j][::-1] in BDICT):
            BDICT[s[:j][::-1]]=1<<60
        if not(s[-j:][::-1] in FDICT):
            FDICT[s[-j:][::-1]]=1<<60

ANS=1<<60
flag=0
for rep in range(1<<60):
    flag=0
    for f in FDICT:
        lf=len(f)
        for s,i in ST:
            ls=len(s)

            if lf == ls:
                if s==f:
                    ANS=min(ANS,FDICT[f]+i)
            elif ls>lf:
                if s[-lf:]==f and BDICT[s[:-lf][::-1]]>FDICT[f]+i:
                    BDICT[s[:-lf][::-1]]=FDICT[f]+i
                    flag=1
            else:
                if f[-ls:]==s and FDICT[f[:-ls]]>FDICT[f]+i:
                    FDICT[f[:-ls]]=FDICT[f]+i
                    flag=1
                    

    for b in BDICT:
        lb=len(b)
        for s,i in ST:
            ls=len(s)

            if lb == ls:
                if s==b:
                    ANS=min(ANS,BDICT[b]+i)
            elif ls>lb:
                if s[:lb]==b and FDICT[s[lb:][::-1]]>BDICT[b]+i:
                    FDICT[s[lb:][::-1]]=BDICT[b]+i
                    flag=1
                    
            else:
                if b[:ls]==s and BDICT[b[ls:]]>BDICT[b]+i:
                    BDICT[b[ls:]]=BDICT[b]+i
                    flag=1
    if flag==0:
        break
                    

for f in FDICT:
    if f==f[::-1]:
        ANS=min(ANS,FDICT[f])

for b in BDICT:
    if b==b[::-1]:
        ANS=min(ANS,BDICT[b])

if ANS==1<<60:
    print((-1))
else:
    print(ANS)

