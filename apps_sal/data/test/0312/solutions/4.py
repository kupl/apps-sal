n, m = (int(x) for x in input().split())
if n == 1:
    print(1)
else:
    if m - 1 >= n - m:
        print(max(1, m - 1))
    else:
        print(min(m + 1, n))
