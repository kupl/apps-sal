def bisect_descending(lst, x):
    l, r = -1, len(lst)
    while r - l > 1:
        m = (r + l) // 2
        if lst[m] > x:
            l = m
        else:
            r = m
    return r


N, Q = list(map(int, input().split()))
row, col = [N], [N]
ans = (N - 2) ** 2
for _ in range(Q):
    n, x = list(map(int, input().split()))
    if n == 1:
        # 下方向
        if x < col[-1]:
            col.append(x)
            row.append(row[-1])
        idx = bisect_descending(col, x)
        ans -= row[idx] - 2
    else:
        # 右方向
        if x < row[-1]:
            row.append(x)
            col.append(col[-1])
        idx = bisect_descending(row, x)
        ans -= col[idx] - 2
print(ans)

