n, m = [int(x) for x in input().split()]
res = 0
if 2 * n >= m:
    res = m // 2
else:
    res = n
    m -= 2 * n
    res += m // 4

print(res)
