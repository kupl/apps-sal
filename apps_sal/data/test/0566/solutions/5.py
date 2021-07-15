c=list(map(int,input().split()))
c.sort()
print(c[0]+c[1] if c[0]+c[1]<=c[2]//2 else sum(c)//3)
