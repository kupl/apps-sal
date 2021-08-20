import sys
from sys import maxsize


def inputint():
    return list(map(int, sys.stdin.readline().strip().split()))


def inputlist():
    return list(map(int, sys.stdin.readline().strip().split()))


def inputstr():
    return list(sys.stdin.readline().strip().split())


def check(s, i, j):
    while i >= 0 and j < len(s):
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            break
    i += 1
    j -= 1
    return j - i + 1


def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    c = 0
    (start, end) = (0, 0)
    for i in range(0, n):
        t1 = check(s, i, i)
        t2 = check(s, i, i + 1)
        c = max(t1, t2)
        if c > end - start:
            start = i - (c - 1) // 2
            end = i + c // 2
    print(end - start + 1)
    print(s[start:end + 1])


solve()
