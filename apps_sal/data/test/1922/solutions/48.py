n, m = list(map(int, input().split()))

if n >= 2 and m >= 2:
    print(((n - 2) * (m - 2)))
    return
if n == 1 and m >= 2:
    print((m - 2))
elif n >= 2 and m == 1:
    print((n - 2))
else:
    print((1))
