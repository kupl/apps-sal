from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    B = [(k - a) % k for a in A]
    C = Counter(B)

    MAX = 1
    IND = -1

    for c in C:
        if c == 0:
            continue
        if MAX < C[c]:
            MAX = C[c]
            IND = c
        elif MAX == C[c] and IND < c:
            IND = c

    print(IND + 1 + (MAX - 1) * k)
