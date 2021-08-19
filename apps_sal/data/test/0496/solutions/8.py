import sys


def solve():
    a = list(map(int, input().split()))
    diffs = list()
    for i in range(3):
        diffs.append(a[i + 1] - a[i])
    if diffs[0] == diffs[1] == diffs[2]:
        return a[3] + diffs[0]
    if a[1] / a[0] == a[2] / a[1] == a[3] / a[2]:
        val = a[3] * diffs[2] / diffs[1]
        if abs(val - int(val)) < 1e-06:
            return int(val)
    return 42


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
print(solve())
