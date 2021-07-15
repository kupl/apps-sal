a,b,c,d=map(int,input().split())
x,y=map(int,input().split())
r=c-a
t=d-b
if r%x==0 and t%y==0 and (r//x-t//y)%2==0:
    print("YES")
else:
    print("NO")
