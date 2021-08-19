(n, s, t) = list(map(int, input().split()))
p = list(map(int, input().split()))
if s == t:
    print(0)
else:
    k = set()
    ans = 0
    while 1:
        s = p[s - 1]
        if s in k:
            print(-1)
            break
        k.add(s)
        ans += 1
        if s == t:
            print(ans)
            break
