t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    ans = n
    for i in range(n):
        if s[i] == '1':
            if i >= n // 2:
                ans = max(ans, 2 * (i + 1))
            else:
                ans = max(ans, (n - i) * 2)
    print(ans)
