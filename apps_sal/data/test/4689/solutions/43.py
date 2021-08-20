import math
import decimal


def i_input():
    return int(input())


def i_map():
    return map(int, input().split())


def i_list():
    return list(map(int, input().split()))


def i_row(N):
    return [int(input()) for _ in range(N)]


def i_row_list(N):
    return [list(map(int, input().split())) for _ in range(N)]


(k, n) = i_map()
aa = i_list()
dis = []
for i in range(n):
    if i == 0:
        dis.append(k - aa[-1] + aa[0])
    else:
        dis.append(aa[i] - aa[i - 1])
print(k - max(dis))
