import bisect
def resolve():
    n = int(input())
    l = sorted(list(map(int,input().split())))
    ans = 0
    for a in range(n):
        for b in range(a+1,n):
            c = bisect.bisect_left(l,l[a]+l[b])
            if c > b:
                ans += c-b-1
            else:
                pass
    print(ans)
resolve()
