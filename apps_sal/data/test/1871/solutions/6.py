(n,x)=list(map(int, input().split()))
c=list(map(int, input().split()))
c.sort()
time=0
for i in range(n):
    time+=x*c[i]
    if x>1:
        x-=1
print(time)

