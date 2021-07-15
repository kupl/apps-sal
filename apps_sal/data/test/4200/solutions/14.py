n,m=map(int,input().split())
a=[*map(int,input().split())];t=sum(a)/(4*m)
print('YNeos'[sum([i>=t for i in a])<m::2])
