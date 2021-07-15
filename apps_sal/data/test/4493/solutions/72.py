c = [list(map(int, input().split())) for _ in range(3)]

diff0 = [x - y for x, y in zip(c[0], c[1])]
diff1 = [x - y for x, y in zip(c[0], c[2])]

if diff0[0] == diff0[1] and diff0[0] == diff0[2] and diff1[0] == diff1[1] and diff1[0] == diff1[2]:
    print('Yes')
else:
    print('No')
