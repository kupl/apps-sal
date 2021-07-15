for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    ans=0
    for i in range(n):
        if l[i]>i:
            ans=i+1
        else:
            break
    print(ans)
