n = int(input())
col_l = 0
col_r = 0
for i in range(n):
    (x, y) = map(int, input().split())
    if x > 0:
        col_r += 1
    else:
        col_l += 1
if col_r > 1 and col_l > 1:
    print('No')
else:
    print('Yes')
