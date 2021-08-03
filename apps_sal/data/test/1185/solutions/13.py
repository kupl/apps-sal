from sys import stdin, setrecursionlimit
from collections import *
import threading


def arr_inp(n):
    if n == 1:
        return [int(x) for x in stdin.readline().split()]
    elif n == 2:
        return [float(x) for x in stdin.readline().split()]
    else:
        return list(stdin.readline()[:-1])


def dp(i, num):
    if num > k:
        return -float('inf')
    if i >= n - m + 1:
        return 0
    if mem[i, num] != -1:
        return mem[i, num]

    mem[i, num] = max(dp(i + 1, num), cum[i] + dp(i + m, num + 1))
    return mem[i, num]


def main():
    ans = 0
    if m == 1:
        print(sum(sorted(a)[n - k:]))
    else:
        for i in range(n - m + 1):
            ans = max(ans, dp(i, 0))

        print(ans)


def __starting_point():
    n, m, k = arr_inp(1)
    a = arr_inp(1)
    mem, cum = defaultdict(lambda: -1), [sum(a[i:i + m]) for i in range(n - m + 1)]
    setrecursionlimit(100000)
    threading.stack_size(102400000)
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
