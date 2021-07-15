N=int(input())
S=input()
x=0
m=0
for i in range(N):
    if S[i]=='(':
        x+=1
    else:
        x-=1
        m=min(x,m)

a=-m
b=x-m
print(('('*a+S+')'*b))

