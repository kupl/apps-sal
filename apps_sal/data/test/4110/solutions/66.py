def solve(D, G, pc):
    point_map = []
    point_sum = []
    for i in range(D):
        p, c = pc[i]
        tmp = [100 * (i + 1)] * p
        tmp[-1] += c
        point_map.append(tmp)
        point_sum.append(sum(tmp))

    ans = 100 * 11
    for i in range(2 ** D):
        count = 0
        point = 0
        other_problems = []
        for j in range(D):
            if i >> j & 1:
                count += pc[j][0]
                point += point_sum[j]
            else:
                other_problems = point_map[j][:-1] + other_problems
        if point < G:
            for op in other_problems:
                count += 1
                point += op
                if point >= G:
                    break
        if point >= G:
            ans = min(ans, count)
    print(ans)


def __starting_point():
    D, G = list(map(int, input().split()))
    pc = [[int(i) for i in input().split()] for _ in range(D)]
    solve(D, G, pc)


__starting_point()
