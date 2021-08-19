import os
import sys


def solve(is_router, k):
    n = len(is_router)
    router_stack = [idx + 1 for (idx, r) in enumerate(is_router) if r == 1][::-1]
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
    (n, k) = list(map(int, input().strip().strip().split()))
    is_router = list(map(int, input().strip()))
    print(solve(is_router, k))


if 'pydev' in sys.argv[0]:
    from string_source import string_source, codeforces_parse
    x = 'inputCopy\n5 2\n00100\noutputCopy\n3\ninputCopy\n6 1\n000000\noutputCopy\n21\ninputCopy\n4 1\n0011\noutputCopy\n4\ninputCopy\n12 6\n000010000100\noutputCopy\n15'
    for (q, a) in codeforces_parse(x):
        pp(string_source(q))
        print(a)
        print('----')
else:
    pp(sys.stdin.readline)
