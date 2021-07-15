q=int(input())
for i in range(q):
    n=int(input())
    a=sorted([int(x) for x in input().split()])
    for i in range(1,n):
        if a[i]==a[i-1]+1:
            print(2)
            break
    else:
        print(1)

