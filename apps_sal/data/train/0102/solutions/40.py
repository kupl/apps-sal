t = int(input())
for i in range(t):
    ns = input()
    n = int(ns)
    ans = 0
    s = ''
    for j in range(1, len(ns) + 1):
        s += '1'
        si = int(s)
        if si > n:
            break
        for k in range(1, 10):
            if si * k <= n:
                ans += 1
            else:
                break
    print(ans)
