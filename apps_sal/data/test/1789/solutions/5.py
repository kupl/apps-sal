a,b,x,y = map(int,input().split())
print(x+min(2*x,y)*(abs(a-b)-(a>b)))
