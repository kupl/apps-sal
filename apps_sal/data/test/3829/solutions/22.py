m, n = list(map(int, input().split()))

ret = m
for i in range(m):
    ret -= pow(i / m, n)

print(ret)
