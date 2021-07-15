import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n,a,b=map(int,input().split())
v=sorted(list(map(int,input().split())),reverse=1)
tmp=sum(v[:a])
ans=(tmp,a)
x=[a-1]
for i in range(a,b):
    tmp+=v[i]
    if ans[0]*(i+1)<=ans[1]*tmp:
        if ans[0]*(i+1)==ans[1]*tmp:
            x.append(i)
        else:
            x=[i]
print(ans[0]/ans[1])
ans=0
for i in x:
    a,b=v.count(v[i]),v[i+1:].count(v[i])
    ans+=comb(a,b)
print(ans)
