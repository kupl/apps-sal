n = int(input())
al = list(map(int, input().split()))
ans = 1

if al.count(0) > 0:
    print(0)
else:
    for a in al:
        ans *= a
        if ans > 10**18:
            print(-1)
            return
    print(ans)
