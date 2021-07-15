def computeLPSArray(pat, M, lps):
    len = 0
    lps[0]
    i = 1

    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def count_subs_occ(s,m,l):
    occ=[0]*(m+1)

    for i in range(m):
        occ[l[i]]+=1

    for i in range(m-1,0,-1):
        occ[l[i-1]]+=occ[i]

    for i in range(m+1):
        occ[i]+=1

    return occ

s=input()
m=len(s)
l=[0]*m

x=computeLPSArray(s,m,l)
x=[0]+x
y=count_subs_occ(s,m,l)

a=x[-1]
if a==0:
    print(1)
    print(m,1)
elif a==1:
    print(2)
    print(1,y[a])
    print(m,1)
else:
    u=x[-1]
    v=x[u]
    ans=[[u,y[u]]]
    while(1):
        if v==0:
            break
        u=v
        v=x[u]
        temp=[u,y[u]]
        ans.append(temp)

    ans.sort()
    print(len(ans)+1)
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])
    print(m,1)
