input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    blocked = []
    binds = []
    b = list(map(int, input().split()))
    for i in range(n):
        if not b[i]:
            blocked += a[i],
            binds += i,
    blocked.sort()
    for i in range(len(binds)):
        a[binds[i]] = blocked[i]
    k1 = -1
    cs = 0
    for i in range(n):
        cs += a[i]
        if cs < 0:
            k1 = i
    ans1 = a.copy()
    blocked.reverse()
    for i in range(len(binds)):
        a[binds[i]] = blocked[i]
    k2 = -1
    cs = 0
    for i in range(n):
        cs += a[i]
        if cs < 0:
            k2 = i
    ans2 = a.copy()
    ans = ans1 if k1 < k2 else ans2
    print(*ans)
