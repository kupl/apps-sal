def ck(a):
    ans = 0
    while a % 2 == 0:
        a = a // 2
        ans += 1
    return([a, ans])


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = {}
    for i in range(n):
        x, y = ck(a[i])
        if c.get(x) == None:
            c[x] = y
        elif c.get(x) < y:
            c[x] = y
    ans = sum(c.values())
    print(ans)
