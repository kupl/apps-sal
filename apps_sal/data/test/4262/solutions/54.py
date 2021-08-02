import math
import itertools
def i_input(): return int(input())


def i_map(): return map(int, input().split())


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


n = i_input()
pp = tuple(i_list())
qq = tuple(i_list())
numls = [i for i in range(1, n + 1)]
patters = list(itertools.permutations(numls, n))
for i in range(len(patters)):
    if pp == patters[i]:
        nmP = i
    if qq == patters[i]:
        nmQ = i
print(abs(nmQ - nmP))
