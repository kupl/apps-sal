t=int(input())

def f():
    n=int(input())
    b=list(map(int,input().split()))
    a=[b[i//2] if i % 2==0 else 0 for i in range(n*2)]
    used = 2*n*[0]+[0]
    for i in a:
        used[i] = 1
    for i in range(1,2*n,2):
        l = a[i-1]
        j=l+1
        while j<=2*n and used[j]:
            j+=1
        if j>2*n:
            print(-1)
            return
        a[i] = j
        used[j]=1
    print(*a)

for tt in range(t):
    f()
