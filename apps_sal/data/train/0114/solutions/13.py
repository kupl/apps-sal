t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = [tuple(map(int, input().split())) for __ in range(m)]
    ans = 1
    mx = [0] * (n + 1)
    for p, s in b:
        mx[s] = max(mx[s], p)
    for i in range(n - 1, -1, -1):
        mx[i] = max(mx[i], mx[i + 1])

    if mx[1] < max(a):
        print(-1)
    else:
        index = 1
        ma = 0
        for mon in a:
            ma = max(mon, ma)
            if mx[index] < ma:
                index = 1
                ans += 1
                ma = mon
            index += 1
        print(ans)
