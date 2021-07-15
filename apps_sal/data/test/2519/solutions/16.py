def resolve():
    n,k = map(int,input().split())
    p = tuple(map(int,input().split()))
    s = [(i+1)/2 for i in p]
    a = sum(s[:k])
    ans = a
    for i in range(1,n-k+1):
        a = a - s[i-1] + s[k+i-1]
        ans = max(ans,a)
    print(ans)
resolve()
