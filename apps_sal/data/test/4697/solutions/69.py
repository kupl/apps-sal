(n, m) = list(map(int, input().split()))
if m >= 2 * n:
    rem = m - 2 * n
    print(n + rem // 4)
else:
    print(m // 2)
