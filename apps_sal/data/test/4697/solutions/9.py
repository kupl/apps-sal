n, m = map(int, input().split())
if 0 <= 2 * n - m:
    num = m // 2
else:
    num = n
    num += (m - 2 * n) // 4
print(num)
