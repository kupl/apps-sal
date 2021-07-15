BEGIN = 'begin'
END = 'end'


def main():
    n = int(input())
    points = dict()

    for _ in range(n):
        li, ri = list(map(int, input().split()))

        update_point_status(points, li, BEGIN)
        update_point_status(points, ri, END)

    points = sorted(list(points.items()), key=lambda x: x[0])
    answer = [0] * (n + 1)

    start = -1
    count = 0
    for point in points:
        points_amount = point[0] - start - 1
        answer[count] += points_amount

        count += point[1][BEGIN]
        answer[count] += 1
        count -= point[1][END]

        start = point[0]

    print(' '.join(list(map(str, answer[1:]))))


def update_point_status(lines, point, status):
    if point not in lines:
        lines[point] = {BEGIN: 0, END: 0}

    lines[point][status] += 1


main()

