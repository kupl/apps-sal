for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    s = list(map(int, list(input())))
    ans = 0
    last1 = n * 2
    for i in range(n):
        if s[i] == 1:
            last1 = i
        elif abs(last1 - i) <= k:
            s[i] = 1
    last1 = n * 2
    for i in range(n - 1, -1, -1):
        if s[i] == 1:
            last1 = i
        elif abs(last1 - i) <= k:
            s[i] = 1
    i = 0
    while i < n:
        if s[i] == 0:
            ans += 1
            i += k + 1
        else:
            i += 1
    print(ans)
