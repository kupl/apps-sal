(n, r) = map(int, input().split())
if n >= 10:
    print(r)
else:
    k = n
    x = r + 100 * (10 - k)
    print(x)
