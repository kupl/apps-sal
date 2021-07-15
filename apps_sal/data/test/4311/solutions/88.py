s=int(input())
def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

a=[0]*(10**8)
a[s]=1
cnt=1
for _ in range(10**7):
    s=f(s)
    cnt+=1
    if a[s]:
        print(cnt)
        break
    a[s]=1

