def f():
    n, m, k = list(map(int, input().split()))
    s = []
    a = []
    for i in range(n):
        s.append(input())
    for j in range(m):
        ans = 0
        for i in range(n):
            if i + i < n and s[i + i][j] == 'U':
                ans += 1
            if j - i >= 0 and s[i][j - i] == 'R':
                ans += 1
            if j + i < m and s[i][j + i] == 'L':
                ans += 1
        a.append(ans)
    print(' '.join(map(str, a)))


f()
