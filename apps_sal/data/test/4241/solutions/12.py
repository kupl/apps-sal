import sys
line_long = sys.stdin.readline().strip()
line_sub = sys.stdin.readline().strip()
len_long = len(line_long)
len_sub = len(line_sub)
min_cnt = len_sub
for idx in range(0, len_long - len_sub + 1):
    this_cnt = 0
    for sub_idx in range(0, len_sub):
        if line_sub[sub_idx] != line_long[sub_idx + idx]:
            this_cnt = this_cnt + 1
    min_cnt = min(min_cnt, this_cnt)
print(min_cnt)
