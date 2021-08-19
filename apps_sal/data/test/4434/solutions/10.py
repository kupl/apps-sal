from itertools import accumulate
import sys
input = sys.stdin.readline
S = [i * 4 * (2 * i) for i in range(5 * 10 ** 5 + 2)]
ANS = list(accumulate(S))
t = int(input())
for tests in range(t):
    n = int(input())
    print(ANS[n // 2])
