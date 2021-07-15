def inpmap():
    return list(map(int, input().split()))
n, m, k = inpmap()
if k < n:
    print(k + 1, 1)
else:
    k -= n
    a, b = divmod(k, (m - 1))
    print(n - a, m - b if a % 2 else b + 2)

