for _ in range(int(input())):
    (n, t) = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = [-1] * n
    if t % 2 == 0:
        x = t // 2
        c = arr.count(x)
        c2 = 0
        for i in range(n):
            if arr[i] != x:
                continue
            if c2 < c // 2:
                ans[i] = 0
            else:
                ans[i] = 1
            c2 += 1
    for i in range(n):
        if ans[i] != -1:
            continue
        if arr[i] <= t // 2:
            ans[i] = 0
        else:
            ans[i] = 1
    print(*ans)
