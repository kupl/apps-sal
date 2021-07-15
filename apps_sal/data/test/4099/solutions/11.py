def resolve():
    n,k,m = map(int,input().split())
    a = tuple(map(int,input().split()))
    ans = n*m - sum(a)
    print(max(ans,0) if ans<=k else -1)
resolve()
