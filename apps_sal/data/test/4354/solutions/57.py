from sys import stdin, stdout


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve():
    n, m = list(map(int, input().split()))
    students = []
    check_points = []

    for _ in range(n):
        a, b = list(map(int, input().split()))
        students.append((a, b))

    for _ in range(m):
        c, d = list(map(int, input().split()))
        check_points.append((c, d))

    for s in students:
        cur_closest_dist = int(4e8)
        cur_closest_point = -1
        for i in range(m):
            c = check_points[i]
            if manhattan_distance(s, c) < cur_closest_dist:
                cur_closest_dist = manhattan_distance(s, c)
                cur_closest_point = i
        print(cur_closest_point + 1)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
