n,a,b = list(map(int,input().split()))
m = min(a,b//(n-1))
for i in range(1,n):
    m = max(m , min(a//i,b//(n-i)))
print(m)

