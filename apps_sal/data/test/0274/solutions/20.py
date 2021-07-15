n = int(input())
s = input()
t = set()
a = [0]*len(s)
q = 0
m = 0
ans = []
for i in range(len(s)):
    if(s[i]=='['):
        q+=1
        a[i]=q
        m=max(m,q)
    else:
        a[i]=q
        q-=1
        m = max(m,q)
        if(s[i-1]=='['):
            t.add(i-1)
for i in range(m+1):
    e=''
    for j in range(len(s)):
        if(a[j]-1==i):
            if(s[j]=='['):
                e+='+-'
                if(j in t):
                    e+=' '
            else:
                e+='-+'
        elif(a[j]-1<i):
            if(s[j]=='['):
                e+='|'
                if(j in t):
                    e+='  '
            elif(s[j]==']'):
                if(j-1 in t):
                    e+=' '
                e+='|'
        else:
            if(s[j]=='['):
                if(j>0 and s[j-1]==']' and a[j-1]==a[j]):
                    e+=' '
                e+=' '
                if(j in t):
                    e+=' '
            else:
                if(j!=len(s)-1 and s[j+1]!=']'):
                    e+=' '
                e+=' '
    ans+=[e]
for i in range(len(ans)):
    print(ans[i])
for i in range(len(ans)-2,-1,-1):
    print(ans[i])


