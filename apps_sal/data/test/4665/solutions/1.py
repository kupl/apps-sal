from collections import namedtuple


def __starting_point():
    s_num = int(input().strip())
    tuple_fields = input().strip().split()
    student = namedtuple('student', tuple_fields)
    library = []
    res = 0
    for _ in range(s_num):
        st_info = input().strip().split()
        library.append(student(st_info[0], st_info[1], st_info[2], st_info[3]))
    for el in library:
        res += int(el.MARKS)
    print(res / s_num)


__starting_point()
