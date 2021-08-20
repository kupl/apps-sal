(n, m) = map(int, input().split())
c = m - n * 2
if c > 0:
    print(n + c // 4)
else:
    print(m // 2)
