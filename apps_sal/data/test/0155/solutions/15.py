n, m, k = list(map(int, input().split(" ")))

if k < n:
    print(k + 1, 1)
else:
    step = k - n
    #print("step:", step)
    row = step // (m - 1) + 1
    col = step % (m - 1)
    reverse = (row % 2 + 1) % 2
    #print("row", row, "col", col, "left", reverse)
    if reverse:
     #   print("rev", col)
        col = (m - 1) - col - 1
    print(n - row + 1, 2 + col)

