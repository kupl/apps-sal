import sys


def solve():
    (n,) = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)
    res = 1
    min_value = a[0]
    for i in range(n):
        min_value = min(min_value, a[i])
        res = max(res, min(i + 1, min_value))
    print(res)


(k,) = list(map(int, sys.stdin.readline().split()))
for _ in range(k):
    solve()
