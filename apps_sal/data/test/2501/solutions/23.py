from collections import Counter
n=int(input())
x=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    a.append(x[i]+i+1)
    b.append((i+1)-x[i])
a,b=Counter(a),Counter(b)
ans=0
for i in range(n):
    ans+=a[i]*b[i]
print(ans)
