n=int(input())
l=list(map(int,input().split()))
sums=0
for i in range(n+1):
    sums+=i
a=sum(l)
if a==sums:
    print('YES')
else:
    print('NO')
    
    
    
