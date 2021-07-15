
for _ in range(int(input())):
    n, m, x, y = list(map(int, input().split()))
    # n = int(input())
    # arr = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        s = input()
        be = s.count('.')
        ch = m - be
        if x * 2 <= y:
            ans += be * x
            continue
        j = 0
        while j < m:
            if s[j] == '*':
                j += 1
                continue
            if j + 1 == m or s[j + 1] == '*':
                ans += x
                j += 1
                continue
            ans += y
            j += 2
    print(ans)

