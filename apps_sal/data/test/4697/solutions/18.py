n, m = list(map(int, input().split()))
if m < 2:
    print((0))
    return
if n > m // 2:
    print((m // 2))
    return
c = n % (m // 2)
d = m - 2 * c
c += d // 4
print(c)
