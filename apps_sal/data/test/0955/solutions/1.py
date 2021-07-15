n = int(input())


costs = [10 ** 18 for i in range(1 << 3)]

for i in range(n):
    cs, s = input().split()
    cs = int(cs)

    msk = 0
    if 'A' in s:
        msk |= 1
    if 'B' in s:
        msk |= 2
    if 'C' in s:
        msk |= 4

    costs[msk] = min(costs[msk], cs)


for msk in [3, 5, 6, 7]:
    for m1 in range(8):
        for m2 in range(8):
            if (m1 | m2) == msk:
                costs[msk] = min(costs[msk], costs[m1] + costs[m2])


if costs[7] == 10 ** 18:
    print(-1)
else:
    print(costs[7])

