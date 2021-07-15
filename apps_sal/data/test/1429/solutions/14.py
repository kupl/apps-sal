from itertools import combinations,permutations,combinations_with_replacement,product,accumulate
n,s=input().split()
n=int(n)
a=[0]*n
t=[0]*n
g=[0]*n
c=[0]*n
for i in range(n):
    if s[i]=="A":
        a[i]+=1
    elif s[i]=="T":
        t[i]+=1
    elif s[i]=="G":
        g[i]+=1
    else:
        c[i]+=1
a=[0]+list(accumulate(a))
t=[0]+list(accumulate(t))
g=[0]+list(accumulate(g))
c=[0]+list(accumulate(c))
ans=0
for i in range(1,n+1):
    for j in range(i+1,n+1,2):
        if (a[j]-a[i-1] == t[j]-t[i-1]) and (g[j]-g[i-1] == c[j]-c[i-1]):
            ans+=1
print(ans)
