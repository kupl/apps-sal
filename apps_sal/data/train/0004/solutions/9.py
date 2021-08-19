t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pos = [0] * (n + 1)
    for (i, x) in enumerate(a):
        pos[x] = i
    used = [0, 1] + [0] * n
    ans = [0] * n
    (l, r) = (pos[1], pos[1])
    count = 1
    for x in range(1, n + 1):
        if not used[x]:
            if pos[x] < l:
                while not used[x]:
                    l -= 1
                    used[a[l]] = 1
                    count += 1
            else:
                while not used[x]:
                    r += 1
                    used[a[r]] = 1
                    count += 1
        if count == x:
            ans[x - 1] = 1
    print(*ans, sep='')
