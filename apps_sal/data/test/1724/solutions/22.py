from sys import stdin
from itertools import accumulate


def arr_enu():
    return [[i, int(x)] for i, x in enumerate(stdin.readline().split())]


def get_col(arr, i):
    return [row[i] for row in arr]


def arr_sum(arr):
    arr.insert(0, 0)
    return list(accumulate(arr, lambda x, y: x + y))


def fun(x, y):
    return int(x) * y[1]


n, a, s = int(stdin.readline()), arr_enu(), stdin.readline()
cum, cum2 = arr_sum(get_col(a, 1)), arr_sum(list(map(fun, s, a)))
ans = cum2[-1]

for i in range(n - 1, -1, -1):
    if s[i] == '1':
        ans = max(ans, cum[i] + (cum2[-1] - cum2[i + 1]))

print(ans)

