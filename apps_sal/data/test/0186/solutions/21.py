n, m = map(int, input().split())

max_m = m * 3
busy_by_m = int(m * 3 / 6)
max_n = (n + busy_by_m) * 2 * bool(n)

nd = 0
md = 0
maxv = 0

if max_n > max_m:
    nd = -2
    md = +3

    max_n_prev = max_n
    max_m_prev = max_m

    for i in range(busy_by_m):
        max_n_prev = max_n
        max_m_prev = max_m
        max_n += nd
        max_m += md
        if max_m % 2 == 0:
            max_m += md
        #print ((max_n_prev, max_m_prev), (max_n, max_m))
        # input()
        if max(max_n_prev, max_m_prev) < max(max_n, max_m):
            break

    maxv = min(max(max_n_prev, max_m_prev), max(max_n, max_m))
else:
    maxv = max_m

print(maxv)
