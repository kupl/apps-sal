a,b,c=map(int,input().split())
x=max(a,b,c)
if x>2*(a+b+c-x):
    print (a+b+c-x)
else:
    print((a+b+c)//3)
