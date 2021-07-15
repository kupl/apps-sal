import os
import sys


def solve(is_router, k):
    n = len(is_router)
    router_stack = [idx + 1 for idx, r in enumerate(is_router) if r == 1][::-1]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        c = dp[i - 1] + i
        while router_stack and router_stack[-1] + k < i:
            router_stack.pop(-1)

        if router_stack and router_stack[-1] - k <= i <= router_stack[-1] + k:
            t = router_stack[-1]
            dp[i] = min(t + dp[max(0, t - k - 1)], c)
        else:
            dp[i] = c

    return dp[-1]


def pp(input):
    n, k = list(map(int, input().strip().strip().split()))
    is_router = list(map(int, input().strip()))
    print(solve(is_router, k))


if "pydev" in sys.argv[0]:
    from string_source import string_source, codeforces_parse

    x = """inputCopy
5 2
00100
outputCopy
3
inputCopy
6 1
000000
outputCopy
21
inputCopy
4 1
0011
outputCopy
4
inputCopy
12 6
000010000100
outputCopy
15"""

    for q, a in codeforces_parse(x):
        pp(string_source(q))
        print(a)
        print("----")
else:
    pp(sys.stdin.readline)

