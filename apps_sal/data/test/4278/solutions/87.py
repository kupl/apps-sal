import sys
input = sys.stdin.readline
from collections import defaultdict


def read():
    N = int(input().strip())
    S = []
    for i in range(N):
        S.append(input().strip())
    return N, S


def solve(N, S):
    words = defaultdict(int)
    for s in S:
        key = "".join(list(sorted(s)))
        words[key] += 1
    
    ans = 0
    for key in words:
        n = words[key]
        if n >= 2:
            ans += n * (n-1) // 2
    return ans


def __starting_point():
    inputs = read()
    print(("%s" % solve(*inputs)))

__starting_point()
