(n, m, k, l) = [int(x) for x in input().split()]
if (l + k) % m == 0:
    c = (l + k) // m
else:
    c = (l + k) // m + 1
if m * c > n:
    print(-1)
else:
    print(c)
