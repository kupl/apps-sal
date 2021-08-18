import statistics

T = int(input())


def cnt(points):
    med = statistics.median(points)
    return int(sum(abs(p - med) for p in points))


for t in range(T):
    N, m = [int(_) for _ in input().split()]
    M = []
    for i in range(N):
        row = [int(_) for _ in input().split()]
        M.append(row)

    answer = 0

    for i in range(N):
        for j in range(m):
            mir_left = m - j - 1
            points = []
            points.append(M[i][j])
            if mir_left > j:
                points.append(M[i][mir_left])
            elif mir_left < j:
                continue
            mir_bot = N - i - 1
            if mir_bot > i:
                points.append(M[mir_bot][j])
            elif mir_bot < i:
                continue
            if mir_left > j and mir_bot > i:
                points.append(M[mir_bot][mir_left])
            answer += cnt(points)

    print(answer)
