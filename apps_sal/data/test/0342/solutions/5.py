a,b,c=map(int,input().split())
print(min(a,b)*2+(1 if a!=b else 0)+c+c)
