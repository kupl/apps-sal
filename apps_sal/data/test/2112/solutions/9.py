n, m = map(int, input().split())
x, k, y = map(int, input().split())
a = [-1] + list(map(int, input().split())) + [-2]
b = [-1] + list(map(int, input().split())) + [-2]
if m > n:
    print(-1)
elif m == n:
    print(-int(a != b))
else:
    g = {}
    for i in range(n + 2):
        g[a[i]] = i
    binds = []
    for i in b:
        if(i not in g) or (binds and binds[-1] > g[i]):
            print(-1)
            return()
        binds.append(g[i])
    # print(binds)
    dels = []
    for i in range(len(binds) - 1):
        dels.append([])
        for j in range(binds[i], binds[i + 1] + 1):
            dels[-1].append(a[j])
    ans = 0
    # print(dels)
    for d in dels:
        todel = len(d) - 2
        if todel:
            mx = max(d)
            allys = max(d[0], d[-1]) == mx
            if y * k < x:
                if allys:
                    ans += todel * y
                else:
                    if todel < k:
                        print(-1)
                        return()
                    ans += y * (todel - k) + x
            else:
                if todel < k:
                    if allys:
                        ans += todel * y
                    else:
                        print(-1)
                        return()
                else:
                    ans += y * (todel % k) + x * (todel // k)
    # print(dels)
    print(ans)
'''
3 1
2 1 1
1 2 3
2
'''
