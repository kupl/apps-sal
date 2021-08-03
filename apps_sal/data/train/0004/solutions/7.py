for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = i

    ans = ''
    mn = 200001
    mx = -1
    for i in range(1, n + 1):
        if(mn > d[i]):
            mn = d[i]
        if(mx < d[i]):
            mx = d[i]

        if(mx - mn + 1 > i):
            ans += '0'

        else:
            ans += '1'

    print(ans)
