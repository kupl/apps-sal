import sys


def count(class_map):
    result = 0

    for row in class_map:
        length = 0
        for seat in row:
            if seat == '.':
                length += 1
            else:
                if length >= k:
                    result += length - k + 1
                length = 0

        if length >= k:
            result += length - k + 1

    return result


n, m, k = list(map(int, sys.stdin.readline().split()))
class_map = [list(line.strip()) for line in sys.stdin]
result = 0

if k == 1:
    for row in class_map:
        for seat in row:
            if seat == '.':
                result += 1
    print(result)
    return


print(count(class_map) + count(list(zip(*class_map))))

