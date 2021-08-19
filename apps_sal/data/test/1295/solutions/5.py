def min_dist_to_tower(a, x):
    (l, r) = (-1, len(a))
    while r - l > 1:
        m = (l + r) // 2
        if a[m] > x:
            r = m
        else:
            l = m
    w = abs(x - a[l]) if l >= 0 else 'SORRY'
    z = abs(x - a[r]) if r < len(a) else 'SORRY'
    if w != 'SORRY' and z != 'SORRY':
        return min(w, z)
    elif w == 'SORRY':
        return z
    else:
        return w


(n, m) = map(int, input().split())
houses = list(map(int, input().split()))
towers = list(map(int, input().split()))
dist = 0
for i in range(len(houses)):
    if min_dist_to_tower(towers, houses[i]) > dist:
        dist = min_dist_to_tower(towers, houses[i])
print(dist)
