for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans="n"
    for i in a:
        for j in b:
            if i==j:
                ans=i
    if ans=='n':
        print("NO")
    else:
        print("YES")
        print("1",ans)
