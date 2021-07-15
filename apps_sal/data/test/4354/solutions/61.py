def distance(coordinate1, coordinate2):
    x1 = coordinate1[0]
    y1 = coordinate1[1]
    x2 = coordinate2[0]
    y2 = coordinate2[1]
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    n, m = map(int, input().split())
    ab_lst = [list(map(int, input().split())) for _ in range(n)]
    cd_lst = [list(map(int, input().split())) for _ in range(m)]
    point_lst = []

    for i in range(n):

        distance_lst = []
        for j in range(m):

            coordinate1 = ab_lst[i]
            coordinate2 = cd_lst[j]
            distance_lst.append(distance(coordinate1, coordinate2))

        minimum = min(distance_lst)
        for k in range(m):
            if distance_lst[k] == minimum:
                point_lst.append(k + 1)
                break

    for i in range(n):
        print(point_lst[i])


def __starting_point():
    main()
__starting_point()
