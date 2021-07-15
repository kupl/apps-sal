a=[int(i) for i in input().split(" ")]
n=a[0]
p=a[1]
k=a[2]
s=[]
a=range(max(1,p-k),min(n+1,p+k+1))
for i in a:
    if(i!=p):
        s.append(str(i))
    else:
        s.append('('+str(i)+')')
if(s[0]!='1' and s[0]!='(1)'):
    s[0]='<< '+s[0]
if(s[-1]!=str(n) and s[-1]!='('+str(n)+')'):
    s[-1]=s[-1]+' >>'
print(" ".join(s))
