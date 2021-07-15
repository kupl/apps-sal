a,b,x,y=map(int,input().split())
if a==b:
    ans=x
elif a<b:
    ans=min(x+(b-a)*y,x*((b-a)*2+1))
else:
    ans=x+min((a-b-1)*y,2*(a-b-1)*x)
print(ans)
