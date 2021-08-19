n = int(input())
for _ in range(n):
    (l, r) = map(int, input().split())
    if (l - r) % 2 == 1:
        if l % 2:
            print((r - l + 1) // 2)
        else:
            print(-((r - l + 1) // 2))
    else:
        ans = 0
        if l % 2:
            ans = ans + (r - l) // 2
        else:
            ans = ans + -(r - l) // 2
        if r % 2:
            ans = ans - r
        else:
            ans = ans + r
        print(ans)
