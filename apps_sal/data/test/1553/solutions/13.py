def can_arrange(heights, h):
    heights = sorted(heights, reverse=True)
    th = 0
    for i in range(0, len(heights), 2):
        th += heights[i]
    return th <= h


n, h = (int(x) for x in input().split())
idx___height = [int(x) for x in input().split()]

l_cl = 0
r_op = n + 1

while r_op - l_cl > 1:
    m = (l_cl + r_op) // 2
    if can_arrange(idx___height[:m], h):
        l_cl = m
    else:
        r_op = m
print(l_cl)
