import sys


def cumsum(li):
    ret = [0]
    sum = 0
    for i in li:
        sum += i
        ret.append(sum)
    return ret


sys.setrecursionlimit(10000)
INF = float('inf')

N = int(input())
A = list(map(int, input().split()))
cs = cumsum(A)
assert len(cs) == N + 1


def calc_diff(d1, d2, d3):
    diffs = [
        cs[d1] - cs[0],
        cs[d2] - cs[d1],
        cs[d3] - cs[d2],
        cs[N] - cs[d3]
    ]
    return max(diffs) - min(diffs)


d0 = 0
d1 = 1
d2 = 2
d3 = 3
d4 = N
ans = INF
while d2 < d4 - 1:
    d012 = abs((cs[d1] - cs[d0]) - (cs[d2] - cs[d1]))
    while d1 < d2 - 1 and d012 > abs((cs[d1 + 1] - cs[d0]) - (cs[d2] - cs[d1 + 1])):
        d1 += 1
        d012 = abs((cs[d1] - cs[d0]) - (cs[d2] - cs[d1]))
    d234 = abs((cs[d3] - cs[d2]) - (cs[d4] - cs[d3]))
    while d3 < d4 - 1 and d234 > abs((cs[d3 + 1] - cs[d2]) - (cs[d4] - cs[d3 + 1])):
        d3 += 1
        d234 = abs((cs[d3] - cs[d2]) - (cs[d4] - cs[d3]))
    ans = min(ans, calc_diff(d1, d2, d3))
    d2 += 1

print(ans)
