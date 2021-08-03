t = int(input())
for i in range(t):
    s = input().split()
    n = int(s[0])
    m = int(s[1])
    if n > m:
        n, m = m, n
    if (2 * n >= m):
        print((n + m) // 3)
    else:
        print(n)
