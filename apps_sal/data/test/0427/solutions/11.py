cnt1, cnt2, x, y = list(map(int, input().split()))

l = 0
r = (cnt1 // (x - 1) + 1) * x + (cnt2 // (y - 1) + 1) * y + 5

while r - l != 1:
    m = l + (r - l) // 2
    t_cnt1 = m // y - m // (x * y)
    t_cnt2 = m // x - m // (x * y)

    if max(0, cnt1 - t_cnt1) + max(0, cnt2 - t_cnt2) <= m - (m // x + m // y - m // (x * y)):
        r = m
    else:
        l = m

print(r)
