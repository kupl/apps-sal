(n, m, k, l) = map(int, input().split())
c = (k + l) // m
if (k + l) % m != 0:
    c += 1
if n >= m * c:
    print(c)
else:
    print(-1)
