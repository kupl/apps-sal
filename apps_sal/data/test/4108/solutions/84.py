s=input()
t=input()
n=len(s)
f=0
a=[[] for i in range(26)]
for i in range(n):
    
    if len(a[ord(s[i])-97])==0:
        a[ord(s[i])-97].append(t[i])
    else:
        if a[ord(s[i])-97][0]!=t[i]:
            f=1
x=[a[i][0] for i in range(26) if len(a[i])==1]
if len(x)!=len(set(x)):
    f=1
print(("Yes" if f==0 else "No"))

    

