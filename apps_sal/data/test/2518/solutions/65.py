import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
n, a, b = list(map(int, input().split()))
a -= b
h = [int(input()) for i in range(n)]


def check(k):
    # k回で可能か?
    tmp = list([x - b * k for x in h])
    return sum(0 - -i // a for i in tmp if i > 0) <= k


ng, ok = 0, 10 ** 18
while ng + 1 < ok:
    mid = (ng + ok) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
