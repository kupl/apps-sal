n, m = map(int, input().split())
for i in range(m):
    if n % 2 == 0 and n // 2 <= (m - i) * 2 - 1:
        x = 1
    else:
        x = 0
    print(i + 1, (m - i) * 2 + i + x)
