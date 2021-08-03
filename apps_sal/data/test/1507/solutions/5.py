n, k = [int(i) for i in input().strip().split()]
g_l = input().strip()

closing_i = dict()
is_closing = [False for i in range(n)]
for i in range(n):
    i = n - i - 1
    if g_l[i] not in closing_i:
        closing_i[g_l[i]] = i
        is_closing[i] = True
open_d = dict()
cur_open = 0
g_open = 0
for i in range(n):
    if g_l[i] not in open_d:
        open_d[g_l[i]] = True
        cur_open += 1
        g_open = max(cur_open, g_open)
    if is_closing[i]:
        cur_open -= 1
if g_open > k:
    print('YES')
else:
    print('NO')
