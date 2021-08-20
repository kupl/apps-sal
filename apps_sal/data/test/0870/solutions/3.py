"""

"""


def read_list():
    return [int(i) for i in input().split()]


def new_list(n):
    return [0 for i in range(n)]


def new_matrix(n, m=0):
    return [[0 for i in range(m)] for i in range(n)]


(d, l, v1, v2) = read_list()
t = l / (v1 + v2)
t -= d / (v1 + v2)
print(t)
