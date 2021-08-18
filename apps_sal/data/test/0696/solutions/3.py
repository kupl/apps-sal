import sys
import fractions


def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount


def solve():
    p = int(input())
    return phi(p - 1)


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
    res = solve()
    write(res)


run()
