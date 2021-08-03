n, m = map(int, input().split())
q = [n, m]
if n == 1 and m == 1:
    print(1)
    return
if 1 in q:
    print(n * m - 2)
    return
if 2 in q:
    print(0)
    return
print((n - 2) * (m - 2))
