def nearest(point):
    l = 0
    r = q
    while r - l > 1:
        mid = int((r + l) / 2)
        if safe[mid] <= point:
            l = mid
        else:
            r = mid
    if safe[l] > point:
        return [safe[l]]
    elif l + 1 == q:
        return [safe[l]]
    else:
        return [safe[l], safe[l + 1]]


def way(come, row, side=True):
    between = abs(right[row] - left[row])
    if side:
        return abs(come - left[row]) + between
    else:
        return abs(come - right[row]) + between


n, m, k, q = [int(x) for x in input().split()]
right = [-1] * n
left = [-1] * n

for i in range(k):
    a, b = [int(x) - 1 for x in input().split()]
    if right[a] == -1:
        right[a] = left[a] = b
    else:
        right[a] = max(right[a], b)
        left[a] = min(left[a], b)
safe = [int(x) - 1 for x in input().split()]
safe.sort()
left[0] = right[0]
if right[0] == -1:
    L = R = min(nearest(0))
    right[0] = left[0] = L
else:
    L = R = right[0]
while right[n - 1] == -1:
    n -= 1
last = 0
for i in range(1, n):
    # print(last)
    # print(L, R)
    L += 1
    R += 1
    if right[i] == -1:
        continue
    left_way = 100000000000
    right_way = 100000000000
    lcolumns = nearest(left[last])
    rcolumns = nearest(right[last])
    for c in lcolumns:
        left_way = min(left_way, L + way(c, i, False) + abs(c - left[last]))
        right_way = min(right_way, L + way(c, i, True) + abs(c - left[last]))
    for c in rcolumns:
        left_way = min(left_way, R + way(c, i, False) + abs(c - right[last]))
        right_way = min(right_way, R + way(c, i, True) + abs(c - right[last]))
    # print(left_way, right_way)
    L = left_way
    R = right_way
    last = i
print(min(L, R))#+ (n - 1))
