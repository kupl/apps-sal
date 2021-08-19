def main():

    N, Ma, Mb = map(int, input().split())
    drug = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        drug.append([a, b, c])

    cur = dict()
    cur[(0, 0)] = 0
    for i in range(N):
        temp = cur.copy()
        for p in cur:
            a, b = p[0] + drug[i][0], p[1] + drug[i][1]

            if (a, b) not in temp:
                temp[(a, b)] = cur[p] + drug[i][2]
            else:
                temp[(a, b)] = min(temp[(a, b)], cur[p] + drug[i][2])
        cur = temp

    # print(cur)
    min_c = float('inf')
    for p in cur:
        if p != (0, 0) and p[0] * Mb == p[1] * Ma:
            min_c = min(min_c, cur[p])
    if min_c == float('inf'):
        return -1
    else:
        return min_c


def __starting_point():
    print(main())


__starting_point()
