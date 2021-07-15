a,b=map(int,input().split())
f=lambda x:[x,1,x+1,0][x%4]
print(f(b)^f(a-1))
