t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    ans = 0
    m = min(l)
    mi = l.index(m)
    for i in range(n):
        if i != mi:
            ans += max((k - l[i]) // m, 0)
    print(ans)
