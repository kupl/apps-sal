import sys


def solve():
    n, m, k = read()
    a = read()
    b = read()
    loc = [0] * (n + 1)
    for i in range(n):
        loc[a[i]] = i
    res = 0
    for i in range(m):
        dist = loc[b[i]] // k
        res += (dist + 1)
        if loc[b[i]] > 0:
            loc[b[i]] -= 1
            val = a[loc[b[i]]]
            loc[val] += 1
            a[loc[b[i]]], a[loc[b[i]] + 1] = a[loc[b[i]] + 1], a[loc[b[i]]]
    return res


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))


def write(s="\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = " ".join(map(str, s))
    if isinstance(s, tuple):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


def run():
    if sys.hexversion == 50594544:
        sys.stdin = open("test.txt")
    res = solve()
    write(res)


run()
