t=int(input())
for w in range(t):
    n,m=(int(i) for i in input().split())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=0
    for i in range(n):
        for j in range(m):
            if(b[j]==a[i]):
                c=1
                k=a[i]
                break
    if(c==0):
        print("NO")
    else:
        print("YES")
        print(1,k)
