from itertools import combinations
import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    S = []
    for i in range(N):
        s = input().strip()
        S.append(s)
    return (N, S)


def solve(N, S):
    Z = [0 for i in range(26)]
    for s in S:
        a = s[0]
        Z[ord(a) - ord('A')] += 1
    ans = 0
    D = [Z[ord(a) - ord('A')] for a in 'MARCH']
    for (i, j, k) in combinations(D, r=3):
        ans += i * j * k
    return ans


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print('%s' % str(outputs))


__starting_point()
