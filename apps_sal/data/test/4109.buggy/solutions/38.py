(nb, na, level) = list(map(int, input().split()))
blevels = []
for i in range(nb):
    blevels.append(list(map(int, input().split())))
ans = float('inf')
for i in range(1, 2 ** nb):
    flag = 0
    levels_sum = [0] * na
    price_sum = 0
    for j in range(nb):
        if 1 << j & i > 0:
            price_sum += blevels[j][0]
            for k in range(1, na + 1):
                levels_sum[k - 1] += blevels[j][k]
    for levels in levels_sum:
        if levels < level:
            flag = 1
            break
    if flag == 0 and ans > price_sum:
        ans = price_sum
if ans != float('inf'):
    print(ans)
else:
    print('-1')
