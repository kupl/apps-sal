from itertools import product, permutations

N, A, B, C = list(map(int, input().split(' ')))
L = [int(input()) for _ in range(N)]

ans = 10 ** 9
for groups in product(list(range(4)), repeat=N):
    items = []
    group_a = []
    group_b = []
    group_c = []

    for group, length in zip(groups, L):
        if group == 0:
            items.append((length, 0))
        elif group == 1:
            group_a.append(length)
        elif group == 2:
            group_b.append(length)
        elif group == 3:
            group_c.append(length)

    if group_a:
        items.append((sum(group_a), (len(group_a) - 1) * 10))
    if group_b:
        items.append((sum(group_b), (len(group_b) - 1) * 10))
    if group_c:
        items.append((sum(group_c), (len(group_c) - 1) * 10))

    if len(items) < 3:
        continue

    for one, two, three in permutations((A, B, C), r=3):
        cost = 0
        _items = list(items)

        _items = sorted(_items, key=lambda x: (abs(x[0] - one), x[1]))
        cost += abs(_items[0][0] - one) + _items[0][1]
        _items.pop(0)

        _items = sorted(_items, key=lambda x: (abs(x[0] - two), x[1]))
        cost += abs(_items[0][0] - two) + _items[0][1]
        _items.pop(0)

        _items = sorted(_items, key=lambda x: (abs(x[0] - three), x[1]))
        cost += abs(_items[0][0] - three) + _items[0][1]

        ans = min(ans, cost)

print(ans)

