n=int(input())
x,y=map(int,input().split())
d1=max(x-1,y-1)
d2=max(n-x,n-y)
if d1<=d2:
    print("White")
else:
    print("Black")
