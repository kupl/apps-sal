def makes( r,l ):
    s=""
    for i in range(r-1):
        s+="0 "
    rl=r+l
    rl2=rl//2
    if rl%2==0:
        s+=str(rl2)+" "
        s+=str(rl2)+" "
    else:
        if r%2==1 :
            s+=str(rl2+1)+" "
            s+=str(rl2)+" "
        if l%2==1 :
            s+=str(rl2)+" "
            s+=str(rl2+1)+" "
    for i in range(l-1):
        s+="0 "
    return s


s = input()
rc=lc=0
ans=""
for i in range(len(s)):
    if s[i]=="R":
        if rc!=0 and lc!=0 :
            ans += makes(rc,lc)
            rc=0
            lc=0
        rc+=1
    else:
        lc+=1
if rc!=0 and lc!=0 :
    ans += makes(rc,lc)
print(ans)
