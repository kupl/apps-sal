n, m = map(int, input().split())
if n == 1:
    print(1)
elif n & 1:
    if (n + 1) // 2 <= m:
        print(m - 1)
    else:
        print(m + 1)
else:
    if n // 2 >= m:
        print(m + 1)
    else:
        print(m - 1)
