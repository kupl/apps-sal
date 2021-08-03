n, m = list(map(int, input().split()))

if n == 1:
    if m == 1:
        print((1))
    else:
        print((m - 2))
elif n == 2:
    print((0))
else:
    if m == 1:
        print((n - 2))
    else:
        print(((n - 2) * (m - 2)))
