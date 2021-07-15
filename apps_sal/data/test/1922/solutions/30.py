import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = list(map(int, input().split()))
if n == 1 and m == 1:
    print((1))
    return
if n == 1:
    print((m - 2))
    return
if m == 1:
    print((n - 2))
    return

print((n * m - (n * 2 + m * 2 - 4)))

