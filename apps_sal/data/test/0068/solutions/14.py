d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def compute_delta(s, head_idx, tail_idx):
    x = y = 0
    for i in range(head_idx, tail_idx):
        (x, y) = (x + d[s[i]][0], y + d[s[i]][1])
    return (x, y)


def compute_rest(s, n, head_idx, tail_idx):
    x = y = 0
    for i in range(0, head_idx):
        (x, y) = (x + d[s[i]][0], y + d[s[i]][1])
    for i in range(tail_idx, n):
        (x, y) = (x + d[s[i]][0], y + d[s[i]][1])
    return (x, y)


n = int(input())
s = input()
(x_d, y_d) = list(map(int, input().split()))
(x_t, y_t) = compute_delta(s, 0, n)
(l, r) = (0, n)
current_sol = -1
while l <= r:
    local_len = (r + l) // 2
    (x_l, y_l) = compute_rest(s, n, 0, local_len)
    is_possible = False
    diff = abs(x_d - x_l) + abs(y_d - y_l)
    if diff <= local_len and (diff + local_len) % 2 == 0:
        is_possible = True
    for i in range(local_len, n):
        if is_possible:
            break
        (d_old, d_new) = (d[s[i]], d[s[i - local_len]])
        (x_l, y_l) = (x_l - d_old[0] + d_new[0], y_l - d_old[1] + d_new[1])
        diff = abs(x_d - x_l) + abs(y_d - y_l)
        if diff <= local_len and (diff + local_len) % 2 == 0:
            is_possible = True
    if is_possible:
        current_sol = local_len
        r = local_len - 1
    else:
        l = local_len + 1
print(current_sol)
