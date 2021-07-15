s=list(input())
ls=len(s)
t=list(input())
lt=len(t)
can=[]
for i in range(ls-lt,-1,-1):
    ok=0
    for j in range(lt):
        if s[i+j]==t[j] or s[i+j]=='?':
            ok+=1
    if ok==lt:
        c=[0]*ls
        for k in range(ls):
            if s[k]=='?':
                if k<i or k>=i+lt:
                    c[k]='a'
                else:
                    c[k]=t[k-i]
            else:
                c[k]=s[k]
        can.append(''.join(c))
if len(can)==0:
    print('UNRESTORABLE')
else:
    print(sorted(list(can))[0])
