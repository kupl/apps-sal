n, k = map(int, input().split())
cnt = 0
for x in range(2, 2 * n + 1):
    if 2 <= x - k <= 2 * n:
        y = x - k
        if x - 1 >= n:
            c1 = max(x - 1 - 2 * (x - 1 - n), 0)
        else:
            c1 = x - 1
        if y - 1 >= n:
            c2 = max(y - 1 - 2 * (y - 1 - n), 0)
        else:
            c2 = y - 1
        cnt += c1 * c2
print(cnt)
