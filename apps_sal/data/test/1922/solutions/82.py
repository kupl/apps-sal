n, m = map(int, input().split())
if n != 1 and m != 1:
    print((n - 2) * (m - 2))
else:
    n, m = max(n, m), min(n, m)
    if m == 1 and n != 1:
        print(n - 2)
    else:
        print(1)
