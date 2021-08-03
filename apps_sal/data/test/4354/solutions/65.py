from typing import List


def manhattan_distance(student: List[int], check_point: List[int]) -> int:
    return abs(check_point[0] - student[0]) + abs(check_point[1] - student[1])


def answer(n: int, m: int, students: List[List[int]], check_points: List[List[int]]) -> str:
    students_destination = []
    for student in students:
        mds = {}
        for i, check_point in enumerate(check_points, start=1):
            md = manhattan_distance(student, check_point)
            if md not in list(mds.keys()):
                mds[md] = str(i)
        students_destination.append(mds[min(mds.keys())])

    return '\n'.join(students_destination)


def main():
    n, m = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(n)]
    cd = [list(map(int, input().split())) for _ in range(m)]
    print((answer(n, m, ab, cd)))


def __starting_point():
    main()


__starting_point()
