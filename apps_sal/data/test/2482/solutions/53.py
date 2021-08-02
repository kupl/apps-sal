from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, K, L = map(int, input().split())


def get_par(x):
    if x == par_list[x]:
        return x
    else:
        par_list[x] = get_par(par_list[x])
        return par_list[x]


def merge(x, y):
    par_x = get_par(x)
    par_y = get_par(y)
    if par_x != par_y:
        par_list[par_y] = par_x


def is_same(x, y):
    return get_par(x) == get_par(y)


par_list = list(range(N + 1))
for _ in range(K):
    p, q = map(int, input().split())
    merge(p, q)
for i in range(1, N + 1):
    par_list[i] = get_par(i)
par_list_road = par_list[:]

par_list = list(range(N + 1))
for _ in range(L):
    r, s = map(int, input().split())
    merge(r, s)
for i in range(1, N + 1):
    par_list[i] = get_par(i)
par_list_rail = par_list[:]

# print(par_list_road)
# print(par_list_rail)
answer_dic = defaultdict(int)
for i in range(1, N + 1):
    road_i = par_list_road[i]
    rail_i = par_list_rail[i]
    answer_dic[(road_i, rail_i)] += 1

answer_list = []
for i in range(1, N + 1):
    road_i = par_list_road[i]
    rail_i = par_list_rail[i]
    answer_list.append(answer_dic[(road_i, rail_i)])

print(*answer_list)
