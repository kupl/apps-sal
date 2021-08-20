(n, m, k) = [int(x) for x in input().split()]
if k < n:
    print(k + 1, 1)
else:
    k -= n
    m -= 1
    i = k // m
    j = k % m
    print(n - i, 2 + j if i % 2 == 0 else m + 1 - j)
