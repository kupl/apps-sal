for __ in range(int(input())):
    n, k = list(map(int, input().split()))
    ans = [[0] * n for i in range(n)]
    i, j = 0, 0
    while k > 0:
        while i < n and k > 0:
            ans[i][j] = 1
            i += 1
            j += 1
            k -= 1
            j %= n
        i = 0
        j += 1
    a1, a2, b1, b2 = 10 ** 9, 0, 10 ** 9, 0
    for i in range(n):
        a1 = min(a1, ans[i].count(1))
        a2 = max(a2, ans[i].count(1))
    for i in range(n):
        kek1 = 0
        for j in range(n):
            if ans[j][i] == 1:
                kek1 += 1
        b1 = min(b1, kek1)
        b2 = max(b2, kek1)
    print((a2 - a1) ** 2 + (b2 - b1) ** 2)
    for elem in ans:
        print(''.join(map(str, elem)))
