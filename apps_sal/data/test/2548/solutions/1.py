from collections import Counter
import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    n = int(input())
    A = input().strip()
    L = []
    for a in A:
        L.append(int(a) - 1)
    SUM = [0]
    for l in L:
        SUM.append(SUM[-1] + l)
    C = Counter(SUM)
    ANS = 0
    for c in C:
        ANS += C[c] * (C[c] - 1) // 2
    print(ANS)
