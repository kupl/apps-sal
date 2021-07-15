#   Yergali B
n=int(input())
s=input()
k=n//4
aa,cc,gg,tt,t,ss=0,0,0,0,0,''
a=sorted(s)
for i in range(0,n):
    if a[i]=='?':
        t+=1
    elif a[i]=='A':
        aa+=1
    elif a[i]=='C':
        cc+=1
    elif a[i]=='G':
        gg+=1    
    elif a[i]=='T':
        tt+=1
if n%4!=0 or aa>k or cc>k or gg>k or tt>k:
    print('===')
else:
    for i in range(0,n):
        if s[i]!='?':
            ss+=s[i]
        else:
            if aa<k:
                ss+='A'
                aa+=1
            elif cc<k:
                ss+='C'
                cc+=1
            elif gg<k:
                ss+='G'
                gg+=1
            elif tt<k:
                ss+='T'
                tt+=1
    print(ss)

