a,b=map(int,input().split(' '))
x,y,z=map(int,input().split(' '))
ans=max(0,2*x+y-a)+max(0,y+3*z-b)
print(ans)
