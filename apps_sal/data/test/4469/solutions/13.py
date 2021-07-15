n=int(input())
ln=0
rn=0
ids={}
bel={}

for i in range(n):
    s=input().split()
    op=s[0]
    id=int(s[1])

    if op=='L' or op=='R':
        if op=='L':
            ln+=1
            ids[id]=ln
            bel[id]='l'
        else:
            rn+=1
            ids[id]=rn
            bel[id]='r'
    else:
        if bel[id]=='l':
             l=ln-ids[id]
             r=ids[id]+rn-1
             print(min(l,r))
        else:
            r=rn-ids[id]
            l=ids[id]+ln-1
            print(min(l,r))


    # if op=='L' or op=='R':
    #     if op=='L':
    #         ln+=1
    #         ids[id]=-ln
    #     else:
    #         rn+=1
    #         ids[id]=rn
    # else:
    #     if ids[id]<0:
    #         ll=ln-abs(ids[id])+1
    #         rr=abs(ids[id])+rn
    #         print(min(ll,rr)-1)
    #     else:
    #         rr=rn-abs(ids[id])+1
    #         ll=abs(ids[id])+rn
    #         print(min(ll,rr)-1)

