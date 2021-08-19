# f = open('test.py')
# def input():
# 	return f.readline().replace('\n','')

# import heapq
# from collections import defaultdict
def read_list():
    return list(map(int, input().strip().split(' ')))


def print_list(l):
    print(' '.join(map(str, l)))


N = int(input())
for _ in range(N):
    n = int(input())
    a = read_list()
    res = 0
    tmp = 0
    s = 0
    for i in range(1, n, 2):
        s += a[i] - a[i - 1]
        res = max(res, s - tmp)
        tmp = min(tmp, s)
    tmp = 0
    s = 0
    for i in range(1, n - 1, 2):
        s += a[i] - a[i + 1]
        res = max(res, s - tmp)
        tmp = min(tmp, s)
    print(sum(a[::2]) + res)
