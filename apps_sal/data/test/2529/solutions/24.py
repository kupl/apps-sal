# cook your dish here

x,y= map(float,input().split())
if(x%5==0):
    x=x+0.5
    if(x<=y):
        y=y-x
print(y)
