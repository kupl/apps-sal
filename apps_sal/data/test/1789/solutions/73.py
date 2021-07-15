a,b,x,y = map(int,input().split())
hoge = max(b-a,a-b-1)
print(min(hoge*x*2,hoge*y)+x)
