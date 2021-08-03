n, a, r, m = [int(x) for x in input().split()]

height = [int(x) for x in input().split()]
hmax = max(height)
height.sort()


def tellCost(h):
    cost = 0
    add, remove = 0, 0
    for i in range(n):
        if h > height[i]:
            add += abs(h - height[i])
        else:
            remove += abs(h - height[i])
    move = min(remove, add)
    if a + r >= m:
        cost += m * move
        if add > remove:
            cost += abs(add - remove) * a
        else:
            cost += abs(add - remove) * r
    else:
        cost += add * a
        cost += remove * r
    return cost


s, e = 0, hmax

while s < e:
    mid = (s + e) // 2
    cost1, cost2 = tellCost(mid), tellCost(mid + 1)
    if cost2 > cost1:
        e = mid
    else:
        s = mid + 1
print(tellCost(s))
