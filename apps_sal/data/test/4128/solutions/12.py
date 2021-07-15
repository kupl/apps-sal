t,*x=map(int,open(0).read().split())
ans=[(y-1)//2 for y in x]
print("\n".join(map(str,ans)))
