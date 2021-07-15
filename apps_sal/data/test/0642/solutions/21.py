inStr=input()
n=int(inStr.split()[0])
m=int(inStr.split()[1])
ans='YES'
if not m==0:
    inStr=input()
    dirty=[int(x) for x in inStr.split()]

    sDirty=sorted(dirty)
    if sDirty[0]==1 or sDirty[-1]==n:
        ans='NO'
    else:
        for i in range(len(sDirty)-2):
            cur=sDirty[i]
            if sDirty[i+1]==cur+1 and sDirty[i+2]==cur+2:
                ans='NO'
                break

print(ans)
