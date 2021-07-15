N,H=map(int,input().split())
a=0
b=[]
for _ in range(N):
    A,B=map(int,input().split())
    a=max(a,A)
    b.append(B)
b=sorted(b,reverse=True)
ans=0
for i in range(N):
    if b[i]<=a:
        break
    H-=b[i]
    ans+=1
    if H<=0:
        print(ans)
        return
print(ans-(-H//a))
