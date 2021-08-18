import sys
import collections


def solve():
    vals = list(input())
    q = collections.deque()
    for cur in vals:
        if len(q) > 0 and q[0] == cur:
            q.popleft()
        else:
            q.appendleft(cur)
    if len(q) == 0:
        return "Yes"
    return "No"


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
