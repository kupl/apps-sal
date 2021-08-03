import sys

input = sys.stdin.readline


def sum1(x):
    k = min(d, c + x - 1, b + x - 1)
    if k < c:
        return 0
    else:
        return (c - b + 1) * (k - c + 1)


def sum2(x):
    k = min(d, c + x - 1)
    l = max(b + x, c)
    if k < l:
        return(0)
    else:
        return (c + x) * (k - l + 1) - (k + l) * (k - l + 1) // 2


a, b, c, d = list(map(int, input().split()))
res = 0
for x in range(a, b + 1):
    res += sum1(x) + sum2(x)
print(res)
