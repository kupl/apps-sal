n,m = map(int,input().split())
#a = [1]*n
i,j = 2,n
for k in range(m):
    x,y = map(int,input().split())
    if x>y:x,y = y,x
    i,j = max(i,x+1), min(j,y)
#print(j-i+1)
print(max(j-i+1,0))
