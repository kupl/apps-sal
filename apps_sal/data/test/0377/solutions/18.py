n, m = (int(i) for i in input().split())
if m > n // 2:
    print(n - m)
else:
    if m:
        print(m)
    else:
        print(1)

