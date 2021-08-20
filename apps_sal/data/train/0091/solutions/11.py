t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    used = []
    for i in range(n):
        used.append(False)
    p = [str(a[0])]
    used[a[0] - 1] = True
    ans = 1
    now = 0
    for i in range(1, n):
        while now < n and used[now]:
            now += 1
        if a[i] > a[i - 1]:
            p.append(str(a[i]))
            if used[a[i] - 1]:
                ans = 0
                break
            used[a[i] - 1] = True
        else:
            if now + 1 > a[i] or used[now]:
                ans = 0
                break
            used[now] = True
            p.append(str(now + 1))
    if ans:
        print(' '.join(p))
    else:
        print(-1)
