from sys import stdin
max_val = int(10000000000000.0)
min_val = int(-10000000000000.0)


def read_int():
    return int(stdin.readline())


def read_ints():
    return [int(x) for x in stdin.readline().split()]


def read_str():
    return input()


def read_strs():
    return [x for x in stdin.readline().split()]


(points, jumps) = read_ints()
print(['NO', 'YES'][len(max(read_str().split('.'), key=len)) < jumps])
