import sys
import random
import copy
from itertools import permutations, combinations
from math import sqrt, fabs, ceil
from collections import namedtuple
in_file_path = 'input.txt'
output_file_path = 'output.txt'
SUBMIT = True


def get_array(x, initial=None):
    dimension = len(x)
    if dimension == 1:
        return [copy.deepcopy(initial) for _ in range(x[0])]
    else:
        return [get_array(x[1:], initial) for _ in range(x[0])]


def read_num(fin, num_type=int):
    tmp_list = [num_type(x) for x in fin.readline().strip().split()]
    if len(tmp_list) == 1:
        return tmp_list[0]
    else:
        return tuple(tmp_list)


def read_num_list(fin, num_type=int):
    return [num_type(x) for x in fin.readline().strip().split()]


def solve(fin):
    n = read_num(fin)
    f = read_num_list(fin)
    new_f = [0] + f
    for i in range(0, n):
        new_f[i] -= 1
    f = new_f
    chs = get_array([n], [])
    for (i, p) in enumerate(f):
        if p >= 0:
            chs[p].append(i)
    q = [x for x in range(0, n) if not chs[x]]
    vis = [0] * n
    count = [0] * n
    while q:
        x = q.pop(0)
        if not chs[x]:
            count[x] = 1
        if f[x] >= 0:
            vis[f[x]] += 1
            if vis[f[x]] == len(chs[f[x]]):
                q.append(f[x])
            count[f[x]] += count[x]
    count = sorted(count)
    print(' '.join([str(x) for x in count]))


def __starting_point():
    if SUBMIT:
        solve(sys.stdin)
    else:
        solve(open(in_file_path, 'r'))


__starting_point()
