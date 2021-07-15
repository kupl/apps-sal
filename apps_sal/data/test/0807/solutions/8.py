n,c  = map(int,input().split())
mal = 0
x = list(map(int,input().split()))
for i in range(n-1):
    if x[i] > x[i+1]+c:
        mal=max(mal,x[i] -x[i+1]-c)
print(mal)
