n, m = map(int, input().split())
if n % 2 == 1:
    for i in range(m):
        print(i + 1, n - i)
else:
    for i in range(m):
        if 2 * (i + 1) <= m + 1:
            print(i + 1, n - i)
        else:
            print(i + 1, n - i - 1)
