n,k = map(int,input().split())
count = 0
if k == 0:
    print(n**2)
    return
for i in range(k+1,n+1):
    count += n//i*(i-k)
    m = n%i
    count += max(m-k+1,0)
print(count)
