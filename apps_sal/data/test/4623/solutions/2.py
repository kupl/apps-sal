from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    W = list(map(int, input().split()))
    C = Counter(W)

    ANS = 0

    for i in range(n):
        for j in range(i + 1, n):
            B = W[i] + W[j]

            A = 0

            for c in C:
                if c * 2 == B:
                    A += C[c] // 2

                elif c * 2 < B:
                    A += min(C[c], C[B - c])

            ANS = max(ANS, A)

    print(ANS)
