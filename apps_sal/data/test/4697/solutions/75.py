n, m = map(int, input().split())

if 2 * n <= m: print(n + (m - 2 * n) // 4)
else: print(m // 2)
