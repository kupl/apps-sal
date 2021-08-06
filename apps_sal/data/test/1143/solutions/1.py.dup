import sys
import datetime


def solve():
    n = int(input())
    count = [0] * 10000
    for i in range(n):
        m, d, p, t = map(int, input().split())
        end = datetime.date(2013, m, d).toordinal() - 734000
        for j in range(end - t, end):
            count[j] += p
    print(max(count))


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
else:
    sys.stdin = open("input.txt")
    sys.stdout = open("output.txt", 'w')
solve()
