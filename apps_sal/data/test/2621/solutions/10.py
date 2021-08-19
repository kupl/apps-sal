from sys import stdin
t = int(stdin.readline().strip())
for case in range(t):
    (n, m, k) = list(map(int, stdin.readline().strip().split()))
    s = list(map(int, stdin.readline().strip().split()))
    t = True
    for j in range(n):
        if j != n - 1:
            x = max(s[j] - max(s[j + 1] - k, 0), 0)
            m += max(s[j] - max(s[j + 1] - k, 0), 0)
            s[j] -= x
            y = max(max(s[j + 1] - k, 0) - s[j], 0)
            m -= y
            if m < 0:
                t = False
            s[j] += y
            if abs(s[j + 1] - s[j]) > k:
                t = False
    if t:
        print('YES')
    else:
        print('NO')
