__author__ = 'Utena'
n=int(input())
s=list(map(int,input().split()))
m=min(s)
a=[]
b=[]
for i in range(n):
    if s[i]==m:
        a.append(i)
for t in range(len(a)-1):
    b.append(a[t+1]-a[t]-1)
b.append(a[0]-a[-1]-1+n)
print(n*m+max(b))
