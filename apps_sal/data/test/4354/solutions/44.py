N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]
cd = [tuple(map(int, input().split())) for _ in range(M)]

for a, b in ab:
    check_point_dist = 10 ** 8 * 4 + 1
    check_point = 0
    count = 0
    for c, d in cd:
        count += 1
        if check_point_dist > abs(a - c) + abs(b - d):
            check_point = count
            check_point_dist = abs(a - c) + abs(b - d)
    else:
        print(check_point)
