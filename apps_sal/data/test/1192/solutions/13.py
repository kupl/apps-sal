import sys

TESTING = False


def reverse(a, l, r):
    res = list(a)
    while l < r:
        res[l], res[r] = res[r], res[l]
        l += 1
        r -= 1
    return res


def inversions(a):
    res = 0
    for l in range(len(a)):
        for r in range(l + 1, len(a)):
            if a[l] > a[r]: res += 1
    return res


def solve():
    n, k = read()
    a = read()
    al = list()
    al.append(list(a))
    for kk in range(k):
        newal = list()
        for val in al:
            for l in range(n):
                for r in range(l, n):
                    newal.append(reverse(val, l, r))
        al = newal;
    res = 0;
    for val in al:
        res += inversions(val)
    return res / len(al)


def read(mode=2):
    inputs = input().strip()
    if mode == 0: return inputs  # String
    if mode == 1: return inputs.split()  # List of strings
    if mode == 2: return list(map(int, inputs.split()))  # List of integers


def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


def run():
    if TESTING: sys.stdin = open("test.txt")
    res = solve()
    write(res)


run()
