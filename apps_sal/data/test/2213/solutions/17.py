def arr_inp(n):
    if n == 1:
        return [int(x) for x in stdin.readline().split()]
    elif n == 2:
        return [float(x) for x in stdin.readline().split()]
    else:
        return [str(x) for x in stdin.readline().split()]


from sys import stdin
from itertools import *

n, m, k = arr_inp(1)
arr, ans = [arr_inp(1) for i in range(n)], list(combinations(list(range(1, m + 1)), 2))
print(len(ans))
for i in range(len(ans)):
    if k:
        print(ans[i][1], ans[i][0])
    else:
        print(ans[i][0], ans[i][1])

