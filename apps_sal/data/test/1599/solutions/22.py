import sys


def solve():
    s = input()
    m = int(input())
    mem = [0] * (len(s) + 1)
    res = list()
    for i in range(1, len(s) + 1):
        mem[i] = mem[i - 1] + (1 if i < len(s) and s[i - 1] == s[i] else 0)
    for query in range(m):
        l, r = map(int, input().split())
        res.append(mem[r - 1] - mem[l - 1])
    print('\n'.join(map(str, res)))


if sys.hexversion == 50594544: sys.stdin = open("test.txt")
solve()
