from collections import defaultdict
(H, W, M) = list(map(int, input().split()))
row_bom_cnt = defaultdict(int)
col_bom_cnt = defaultdict(int)
row_max = 0
col_max = 0
boms = [list(map(int, input().split())) for _ in range(M)]
for (rm, cm) in boms:
    row_bom_cnt[rm] += 1
    col_bom_cnt[cm] += 1
    row_max = max(row_max, row_bom_cnt[rm])
    col_max = max(col_max, col_bom_cnt[cm])
target_row = set()
for (r, val) in list(row_bom_cnt.items()):
    if val == row_max:
        target_row.add(r)
target_col = set()
for (c, val) in list(col_bom_cnt.items()):
    if val == col_max:
        target_col.add(c)
cnt = 0
for (rm, cm) in boms:
    if rm in target_row and cm in target_col:
        cnt += 1
if len(target_row) * len(target_col) == cnt:
    print(row_max + col_max - 1)
else:
    print(row_max + col_max)
