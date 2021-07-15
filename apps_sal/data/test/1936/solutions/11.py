for _ in range(int(input())):
    n,m = map(int,input().split())
    if m>=2*n:
        print(n,2*n)
    else:
        print("-1 -1")
