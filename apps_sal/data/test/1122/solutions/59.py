n, m = map(int, input().split())

if m % 2 == 0:
    for i in range(m // 2):
        print(1 + i, m - i)
        print(m + 1 + i, 2 * m + 1 - i)
else:
    for i in range((m // 2) + 1):
        print(m + 1 + i, 2 * m + 1 - i)
    for i in range(m // 2):
        print(1 + i, m - i)
