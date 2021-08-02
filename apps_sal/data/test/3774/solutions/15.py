n, m = [int(i) for i in input().split()]
m, n = max(m, n), min(n, m)
a = m * n
if m == 7 and n == 2:
    print(12)
    return
if m == 3 and n == 2:
    print(4)
    return
if n == 1:
    print(a - min(m % 6, 6 - m % 6))
else:
    if m * n >= 6:
        print(n * m - (n * m) % 2)
    else:
        print(0)
