(n, m) = list(map(int, input().strip().split()))
if n >= m:
    if m % 2 == 0:
        print((m - 2) // 2)
    else:
        print((m - 1) // 2)
else:
    if m % 2 == 0:
        l1 = (m - 2) // 2
        l1 = l1 - (m - n - 1)
    else:
        l1 = (m - 1) // 2
        l1 = l1 - (m - n - 1)
    if l1 <= 0:
        print(0)
    else:
        print(l1)
