n,k=list(map(int,input().split()))
a=set()
for i in range(1,k+1):
    if n%i in a:
        print('No')
        return
    else:
        a.add(n%i)
print('Yes')

