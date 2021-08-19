for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    (ans, small, big) = (0, 2 * 10 ** 9, -1)
    for i in range(len(a) - 1):
        if a[i] == -1 and a[i + 1] != -1:
            small = min(small, a[i + 1])
            big = max(big, a[i + 1])
        if a[i] != -1 and a[i + 1] == -1:
            small = min(small, a[i])
            big = max(big, a[i])
        if a[i] != -1 and a[i + 1] != -1:
            ans = max(ans, abs(a[i] - a[i + 1]))
    if big == -1:
        print(ans, 0)
    else:
        x = (small + big) // 2
        ans = max(ans, abs(big - x))
        ans = max(ans, abs(x - small))
        print(ans, x)
