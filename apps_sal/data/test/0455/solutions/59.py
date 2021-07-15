inf = float('inf')

n = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(n)]

parity = None
can_make = True
for coordinate in coordinates:
    if parity is None:
        parity = sum(coordinate) % 2
    else:
        if parity != sum(coordinate) % 2:
            can_make = False
            break

if not can_make:
    print(-1)
    return
    # 到達可能な頂点はxy座標の和のパリティが一致している必要がある

m = 40
if parity == 0:
    d = [pow(2, i) for i in range(39)] + [1]
    # 奇数は1だけなので、1を追加して、全ての腕の合計が偶数になるようにする
else:
    d = [pow(2, i) for i in range(40)]
    # 奇数は1だけなので、全ての腕の合計は奇数になる
d.sort(reverse=True)

ans = []
for x, y in coordinates:
    curx, cury = 0, 0
    ops = ''
    for dd in d:
        dist = inf
        op = ''
        det_dx, det_dy = 0, 0
        for c, (dx, dy) in zip('LRDU', [(-1, 0), (1, 0), (0, -1), (0, 1)]):
            t = abs(curx + dx * dd - x) + abs(cury + dy * dd - y)
            if dist > t:
                op = c
                dist = t
                det_dx = dx
                det_dy = dy
        ops += op
        curx += det_dx * dd
        cury += det_dy * dd
    if (curx, cury) == (x, y):
        ans.append(ops)
    else:
        print(-1)
        # print('不一致', curx, cury, x, y)

print(m)
print(*d)
print(*ans, sep='\n')

