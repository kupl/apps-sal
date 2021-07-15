n, m, k = map(int, input().split())
if k < n:
    print(k + 1, 1)
else:
    k -= n
    row = n - k // (m - 1)
    col = k % (m - 1)
    if row % 2 == 1:
        col = m - col
    else:
        col += 2
    print(row, col)
