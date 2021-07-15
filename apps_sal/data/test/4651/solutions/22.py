for _ in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    ans, i = [], 0
    while a:
        m = min(a)
        x = a.index(m)
        ans.append(m)
        if x == 0:
            a.remove(m)
            continue
        ans += a[:x - 1]
        a = a[x - 1:]
        if m in a:
            a.remove(m)
        
    print(*ans)
