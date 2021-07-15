k=int(input())
x,y=map(int,input().split())

if k%2==0 and (x+y)%2!=0:
    print(-1)
    return

def f(x,y):
    if x<0:
        a,b=f(-x,y)
        return -a,b
    if y<0:
        a,b=f(x,-y)
        return a,-b
    if x<y:
        a,b=f(y,x)
        return b,a
    if x+y==k:
        return x,y
    if x+y<=k*2 and (x+y)%2==0:
        return (x+y)//2,(x+y)//2-k
    return k,0

p,q=0,0
ans=[]
while (p,q)!=(x,y):
    a,b=f(x-p,y-q)
    p+=a
    q+=b
    ans.append(str(p)+" "+str(q))

print(len(ans))
print('\n'.join(ans))
