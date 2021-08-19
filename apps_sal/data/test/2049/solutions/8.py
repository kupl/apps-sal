import sys


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def input():
    return sys.stdin.readline().strip()


(n, m) = get_ints()
Arr = get_array()
up = [i for i in range(n)]
down = [i for i in range(n)]
for i in range(1, n):
    if Arr[i - 1] <= Arr[i]:
        up[i] = up[i - 1]
    if Arr[i - 1] >= Arr[i]:
        down[i] = down[i - 1]
while m:
    (l, r) = get_ints()
    if l - 1 >= up[down[r - 1]]:
        print('Yes')
    else:
        print('No')
    m -= 1
