
n, k = map(int, input().split())
p = [int(x) - 1 for x in input().split()]
c = [int(x) for x in input().split()]
pow_num = 31
point = [[0] * n for i in range(pow_num)]
point_max = [[0] * n for i in range(pow_num)]
posi = [[0] * n for i in range(pow_num)]

c_set = set(c)
if all([i < 0 for i in c_set]):
    print(max(c_set))
else:
    for i in range(pow_num):
        if i == 0:
            for j in range(n):
                posi[i][j] = p[j]
                point[i][j] = c[p[j]]
            continue
        for j in range(n):
            posi[i][j] = posi[i - 1][posi[i - 1][j]]
            point[i][j] = point[i - 1][j] + point[i - 1][posi[i - 1][j]]
    for i in range(pow_num):
        if i == 0:
            for j in range(n):
                point_max[i][j] = point[i][j]
            continue
        for j in range(n):
            point_max[i][j] = max(point_max[i - 1][j],
                                  point[i - 1][j] + point_max[i - 1][posi[i - 1][j]])

    power_count = list()
    for i in range(pow_num):
        if k & (1 << i):
            power_count.append(i)

        ans = 0
        for i in range(n):
            next_posi = i
            cumsum_point = 0
            for posi_idx in power_count:
                if ans < cumsum_point + point_max[posi_idx][next_posi]:
                    ans = cumsum_point + point_max[posi_idx][next_posi]
                cumsum_point += point[posi_idx][next_posi]
                next_posi = posi[posi_idx][next_posi]

    print(ans)
