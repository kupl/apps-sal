import sys


def solve():
    n = list(input())
    for i in range(len(n)):
        if int(n[i]) > 4 and (i != 0 or int(n[i]) != 9):
            n[i] = str(9 - int(n[i]))
    return n


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs  # String
    if mode == 1:
        return inputs.split()  # List of strings
    if mode == 2:
        return list(map(int, inputs.split()))  # List of integers


def write(s="\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = "".join(map(str, s))
    if isinstance(s, tuple):
        s = "".join(map(str, s))
    s = str(s)
    print(s, end="")


def run():
    if sys.hexversion == 50594544:
        sys.stdin = open("test.txt")
    res = solve()
    write(res)


run()
